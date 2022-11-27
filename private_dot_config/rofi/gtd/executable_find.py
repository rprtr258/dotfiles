#!/usr/bin/env python3

from sys import argv
from subprocess import check_output

from common import GTD_DIR

if len(argv) == 1:
    pass
else:
    param = argv[1]
    # TODO: open file
    print(check_output(["rg", param, "-i", "--hidden"], cwd=GTD_DIR).decode(errors="ignore"))
