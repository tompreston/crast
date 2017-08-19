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
import os.path
import argparse
import mimetypes
import pychromecast


DESCRIPTION = 'crast is a simple interface to pychromecast'
EPILOGUE = '''
crast Copyright (C) 2017 Thomas Preston <thomasmarkpreston@gmail.com>
This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
This is free software, and you are welcome to redistribute it
under certain conditions; type `show c' for details.
'''


def get_chromecast(friendly_name=None):
    '''Returns the named Chromecast or the first one found.'''
    print('Searching for devices')
    ccasts = pychromecast.get_chromecasts()
    if args.device:
        cast = next(cc for cc in ccasts
                if cc.device.friendly_name == args.device)
    else:
        cast = ccasts[0]
    cast.wait()

    return cast;


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description=DESCRIPTION, epilog=EPILOGUE)
    parser.add_argument('url', help='A URL to cast')
    parser.add_argument('-d', '--device', help='A device to cast to')
    args = parser.parse_args()

    url_type, url_encoding = mimetypes.guess_type(args.url)
    url_basename = os.path.basename(args.url)
    cast = get_chromecast(args.device)

    print('Casting to {}'.format(cast.device.friendly_name))
    print(url_basename)
    print(url_type)

    mc = cast.media_controller
    mc.play_media(args.url, url_type, title=url_basename)
    mc.block_until_active()

