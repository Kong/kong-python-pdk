
Schema = (
    { "message": { "type": "string" } },
)

# This is an example plugin that add a header to the response

class Plugin(object):
    def __init__(self, config):
        self.config = config

    def access(self, kong):
        host, err = kong.request.get_header("host")
        if err:
            kong.log.err(err)
        message = "hello"
        if 'message' in self.config:
            message = self.config['message']
        kong.response.set_header("x-hello-from-python", "Python says %s to %s" % (message, host))