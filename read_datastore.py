#!/usr/bin/env python
# -*- coding: us-ascii -*-
# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab
#
# Python version of read_datastore.sh from https://github.com/dbeley/shaarli-import-datastore

import base64

try:
    #raise ImportError()
    # Python 2.6+
    import json
except ImportError:
    try:
        #raise ImportError()
        # from http://code.google.com/p/simplejson
        import simplejson as json
    except ImportError:
        json = None

import sys
import zlib

import phpserialize  # https://github.com/mitsuhiko/phpserialize


try:
    filename = sys.argv[1]
except  IndexError:
    filename = 'datastore.php'


f = open(filename, 'rb')
data = f.read()  # read all into memory
f.close()

# dumb strip/extract base64 string from php code comment
data = data.replace(b'<?php /* ', b'')
data = data.replace(b' */ ?>', b'')
d = base64.decodestring(data)
#print(repr(d))


# Python equivalent of PHP gzinflate()
raw_data = zlib.decompressobj().decompress(b'x\x9c' + d)
#print(repr(raw_data))

def object_hook(name, value):
    #print('hook %r', ((name, value),))
    #assert name == b'DateTime'
    assert name in (b'DateTime', 'DateTime')
    #return value[b'date']  # return as-is
    return value  # return as-is

#the_data = phpserialize.loads(raw_data, object_hook=phpserialize.phpobject)  # will not fail, but does not deserialize date, ends up missing
the_data = phpserialize.loads(raw_data, object_hook=object_hook, decode_strings=True)
print(json.dumps(the_data, indent=4))

