"""Simple interface to pychromecast
Copyright (C) 2017 Thomas Preston <thomasmarkpreston@gmail.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import argparse
import mimetypes
import os.path
import sys

import pychromecast

DESCRIPTION = "crast is a simple interface to pychromecast"
EPILOGUE = """
crast Copyright (C) 2017 Thomas Preston <thomasmarkpreston@gmail.com>
This program comes with ABSOLUTELY NO WARRANTY; for details type `show w".
This is free software, and you are welcome to redistribute it
under certain conditions; type `show c" for details.
"""
CMDS = ("play", "pause", "stop", "skip", "rewind")

def parse_args():
    """Returns a populated argument namespace."""
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=DESCRIPTION, epilog=EPILOGUE)
    parser.add_argument("-u", "--url", help="A URL to cast")
    parser.add_argument("-d", "--device-name",
                        help="The device to control (fuzzy search UUID or "
                             "Friendly name)")
    parser.add_argument("-c", "--command", help="Send a command", choices=CMDS)
    parser.add_argument("-s", "--status", help="Print the device status",
                        action="store_true")
    return parser.parse_args()

def pr_chromecasts(cc):
    """Print useful information about Chromecasts."""
    if cc:
        print("{u:>8} {fname}".format(u="UUID", fname="Friendly name"))
    for c in cc:
        print("{:x} {}".format(c.device.uuid.fields[0], c.device.friendly_name))

def is_chromecast(c, uuid_or_frname):
    """Returns True if Chromecast c matches UUID or Friendly name. The match is
    fuzzy, so partial matches also return True:

        Living in "Living Room TV"
        L in "Living Room TV"
        877c6398 in "877c6398-XXXX-XXXX-XXXX-XXXXXXXXXXXX"

    """
    for propery in str(c.device.uuid), c.device.friendly_name:
        if uuid_or_frname in propery:
            return True
    return False

def search_chromecasts(device_name):
    """Search for Chromecasts on the network, print and filter them, then
    return the first one found.
    """
    print("Searching for Chromecasts")
    cc = pychromecast.get_chromecasts()
    if not cc:
        print("No Chromecast found")
        return None

    pr_chromecasts(cc)
    print()

    if device_name:
        cc = list(filter(lambda d: is_chromecast(d, device_name), cc))
        if not cc:
            print(f"Could not find {device_name}")
            return None

    return cc[0]

def play_media_url(cast, url):
    """Tell Chromecast to play media from a url."""
    url_type, url_encoding = mimetypes.guess_type(url)
    url_basename = os.path.basename(url)
    print("Playing media")
    print(url_basename)
    print(url_type, url_encoding)

    mc = cast.media_controller
    mc.play_media(url, url_type, title=url_basename)

def command_chromecast(c, command):
    """Send a command to a Chromecast."""
    mc = c.media_controller
    mc.block_until_active()
    try:
        getattr(mc, command)()
    except AttributeError:
        print("Unknown command")
    else:
        print(command)

def pr_status(c):
    """Print the status of a Chromecast."""
    for a in "uuid", "friendly_name", "model_name", "manufacturer", "cast_type":
        print("{:>13} {}".format(a, getattr(c.device, a)))
    for a in "uri", "is_idle", "app_id", "app_display_name":
        print("{:>13} {}".format(a, getattr(c, a)))

def crast(args):
    """Control a Chromecast."""
    c = search_chromecasts(args.device_name)
    if not c:
        print("No Chromecast selected, aborting")
        sys.exit(1)

    print(f"Using '{c.device.friendly_name}'")

    if args.url:
        play_media_url(c, args.url)
    if args.command:
        command_chromecast(c, args.command)
    if args.status:
        pr_status(c)

if __name__ == "__main__":
    crast(parse_args())
