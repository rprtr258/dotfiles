#!/usr/bin/env python3
from sys import argv
from urllib.parse import urlencode

from gtd.common import my_open

if len(argv) == 1:
    # TODO: recent searches?
    pass
else:
    param = argv[1]
    # TODO: different search engines: google, yandex, google images, yandex images, iqdb, docs
    my_open("https://google.com/search?" + urlencode({"q": param}))
