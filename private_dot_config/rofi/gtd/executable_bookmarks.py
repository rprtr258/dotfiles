#!/usr/bin/env python3
from os import path
from sys import argv
from configparser import ConfigParser

from common import GTD_DIR, my_open

if len(argv) == 1:
    c = ConfigParser()
    c.read(path.join(GTD_DIR, "reference/", "browser_bookmarks.ini"))
    for section in c.sections():
        for key, url in c[section].items():
            print(f"{section}/{key}: {url}")
else:
    param = argv[1]
    my_open(param[param.index(": ") + len(": "):])
