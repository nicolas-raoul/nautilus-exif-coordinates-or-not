#####################################################################
#                                                                   #
# Copyright 2016, Chris Billington, Nicolas Raoul                   #
#                                                                   #
# This file is part of the git-nautilus-icons project (see          #
#  https://github.com/chrisjbillington/git_nautilus_icons) and is   #
# licensed under the Simplified BSD License. See LICENSE in         #
# the root directory of the project for the full license.           #
#                                                                   #
#####################################################################

from __future__ import print_function, unicode_literals
import sys
import os
import pathlib
from enum import IntEnum, unique
import gi
from gi.repository import GObject
if sys.argv[0] == 'nemo':
    gi.require_version('Nemo', '3.0')
    from gi.repository import Nemo as Nautilus
elif sys.argv[0] == 'caja':
    gi.require_version('Caja', '2.0')
    from gi.repository import Caja as Nautilus
else:
    gi.require_version('Nautilus', '3.0')
    from gi.repository import Nautilus
from subprocess import Popen, PIPE, CalledProcessError
from collections import defaultdict
from exifread import process_file
from exifread.tags import DEFAULT_STOP_TAG

def get_filepath(file):
    """Extract filepath from the URI in a NautilusVFSFile object. Return the
    filepath or None if uri scheme is not 'file'"""
    if sys.version_info.major == 2:
        from urlparse import urlparse
        from urllib import unquote
    else:
        from urllib.parse import urlparse
        from urllib.parse import unquote

    parsed_uri = urlparse(file.get_uri())
    if parsed_uri.scheme == 'file':
        netloc = parsed_uri.netloc.decode('utf8')
        path = unquote(parsed_uri.path).decode('utf8')
        return os.path.abspath(os.path.join(netloc, path))

class InfoProvider(GObject.GObject, Nautilus.InfoProvider):
    def update_file_info(self, file): # file seems to be a Nautilus.FileInfo object

	# We only care about local files
	if file.get_uri_scheme() != 'file':
	    print("URI scheme is not file")
            return

	# We only care about images
	if file.get_mime_type() in ('image/jpeg'):
	    filepath = get_filepath(file)
	    print("Checking whether this picture has an EXIF longitude: " + filepath)
	    openedFile = open(filepath)
	    
	    detailed = True
	    stop_tag = "GPS GPSLongitude"
	    debug = True
	    strict = False
	    color = False
            data = process_file(openedFile, stop_tag=stop_tag, details=detailed, strict=strict, debug=debug)

	    if 'GPS GPSLongitude' in data:
		file.add_emblem("new") # TODO Find better icon for GPS EXIF presence and add per https://stackoverflow.com/questions/27628241/python-nautilus-add-custom-emblems-overlay-icon
