#!/usr/bin/env python3

from glob import glob
from os import path, listdir
from sys import argv

from common import IN_DIR, my_open


if len(argv) == 1:
    for filename in listdir(IN_DIR):
        full_filename = path.join(IN_DIR, filename)
        if path.isfile(full_filename) and full_filename.endswith(".md"):
            with open(full_filename) as fd:
                content_line = ' '.join(fd.read().split()).strip()
                print(f"{filename}: {content_line}")
        else:
            print(f"{filename}")
else:
    param = argv[1]
    # TODO: open dir
    if ".md" in param:
        my_open(path.join(IN_DIR, param[:param.index(": ")]))
    elif ".md: " not in param:
        words = param.split()
        with open(path.join(IN_DIR, path.basename(f"{words[0]}.md")), 'a+') as fd:
            fd.write(param)
            fd.write("\n")
