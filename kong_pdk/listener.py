import asyncio
import msgpack
import os
import sys
from concurrent.futures import ProcessPoolExecutor
from functools import partial
from .exception import PDKException, PluginServerException

class AsyncPluginServer:
    def __init__(self, plugin_server, use_multiprocess=False, max_workers=None):
        self.ps = plugin_server
        self.logger = plugin_server.logger
        self.use_multiprocess = use_multiprocess
        if use_multiprocess:
            self.process_pool = ProcessPoolExecutor(max_workers=max_workers)

    async def handle_client(self, reader, writer):
        unpacker = msgpack.Unpacker(strict_map_key=False)

        while True:
            try:
                message = await reader.read(1024)
                if not message:
                    break

                unpacker.feed(message)
                for unpacked in unpacker:
                    _, msgid, method, args = unpacked
                    ns, cmd = method.split(".")
                    
                    if ns != "plugin":
                        await self.write_error(writer, msgid, f"RPC for {ns} is not supported")
                        continue

                    cmd_r = cmd[0].lower() + ''.join([c.lower() if c.islower() else f"_{c.lower()}" for c in cmd[1:]])
                    
                    try:
                        self.logger.debug(f"rpc: #{msgid} method: {method} args: {args}")
                        if self.use_multiprocess and cmd_r in ['handle_event', 'step', 'step_error']:
                            # Use ProcessPoolExecutor for potentially CPU-bound operations
                            loop = asyncio.get_running_loop()
                            ret = await loop.run_in_executor(
                                self.process_pool, 
                                partial(getattr(self.ps, cmd_r), *args)
                            )
                        else:
                            ret = await getattr(self.ps, cmd_r)(*args)
                        self.logger.debug(f"rpc: #{msgid} return: {ret}")
                        await self.write_response(writer, msgid, ret)
                    except (PluginServerException, PDKException) as ex:
                        self.logger.warn(f"rpc: #{msgid} error: {str(ex)}")
                        await self.write_error(writer, msgid, str(ex))
                    except MemoryError as ex:
                        self.logger.error(f"rpc: #{msgid} exception: {str(ex)}")
                        await self.write_error(writer, msgid, str(ex))

            except asyncio.CancelledError:
                break
            except MemoryError as e:
                self.logger.error(f"Error handling client: {str(e)}")
                break

        writer.close()
        await writer.wait_closed()

    async def write_response(self, writer, msgid, response):
        writer.write(msgpack.packb([1, msgid, None, response]))
        await writer.drain()

    async def write_error(self, writer, msgid, error):
        writer.write(msgpack.packb([1, msgid, error, None]))
        await writer.drain()

    def cleanup(self):
        if self.use_multiprocess:
            self.process_pool.shutdown(wait=True)

async def start_async_server(plugin_server, socket_path, use_multiprocess=False, max_workers=None):
    server = AsyncPluginServer(plugin_server, use_multiprocess, max_workers)
    
    # Remove the socket file if it already exists
    try:
        os.unlink(socket_path)
    except OSError:
        if os.path.exists(socket_path):
            raise

    # Start the server
    unix_server = await asyncio.start_unix_server(server.handle_client, path=socket_path)

    plugin_server.logger.info(f"Async server started at path {socket_path}")
    plugin_server.logger.info(f"Multiprocessing: {'Enabled' if use_multiprocess else 'Disabled'}")

    async with unix_server:
        await unix_server.serve_forever()

# Watchdog function to monitor parent process
async def watchdog(plugin_server):
    while True:
        if os.getppid() == 1:  # parent dead, process adopted by init
            plugin_server.logger.info("Kong exits, terminating...")
            sys.exit()
        await asyncio.sleep(1)

# Main function to start the server and watchdog
async def run_server(plugin_server, socket_path, use_multiprocess=False, max_workers=None):
    # Start the watchdog
    watchdog_task = asyncio.create_task(watchdog(plugin_server))
    
    # Start the server
    server_task = asyncio.create_task(start_async_server(plugin_server, socket_path, use_multiprocess, max_workers))
    
    try:
        # Wait for both tasks
        await asyncio.gather(watchdog_task, server_task)
    finally:
        # Ensure cleanup is performed
        if use_multiprocess:
            server_task.result().cleanup()