#!/usr/bin/env python3

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import io

version = '0.1.0'
priority = 0

# This is an example plugin that uses PIL to generate an PNG image
# containing text of the request headers
# Run the following commands first:
'''
sudo apt install ttf-mscorefonts-installer
sudo apt install font-manager
sudo fc-cache -f -v
'''

class Plugin(object):
    def __init__(self, config):
        self.config = config

    def access(self, kong):
        img = Image.new("RGB", (800, 200))
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("Comic_Sans_MS.ttf", 24)
        y = 0
        headers, _ = kong.request.get_headers()
        for h in headers:
            y = y + 32
            draw.text((0, y), "%s: %s" % (h, headers[h]), (255,255,255), font=font)
        b = io.BytesIO()
        img.save(b, format='PNG')
        kong.response.exit(200,
            b.getvalue()
        )

# add below section to allow this plugin optionally be running in a dedicated process
if __name__ == "__main__":
    from kong_pdk.cli import start_dedicated_server
    start_dedicated_server("py-image", Plugin, version, priority)