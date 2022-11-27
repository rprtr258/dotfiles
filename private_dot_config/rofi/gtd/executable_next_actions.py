#!/usr/bin/env python3

from sys import argv
from glob import glob
from os import path

from common import NEXT_ACTIONS_DIR


if len(argv) == 1:
    for filename in glob(path.join(NEXT_ACTIONS_DIR, "*.md")):
        with open(filename) as fd:
            relative_filename = path.relpath(filename, NEXT_ACTIONS_DIR)
            print(f"{relative_filename}: {fd.readline()}")
else:
    param = argv[1]
    # TODO: open file/clip content
    pass
