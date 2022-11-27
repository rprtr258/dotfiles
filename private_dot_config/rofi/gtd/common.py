from os import path, setpgrp
from subprocess import Popen

GTD_DIR = "/home/rprtr258/GTD/"
IN_DIR = path.join(GTD_DIR, "in/")
NEXT_ACTIONS_DIR = path.join(GTD_DIR, "next_actions/")
CALENDAR_DIR = path.join(GTD_DIR, "calendar/")

def run(*args):
    Popen(args, stdout=open("/dev/null", "w"), stderr=open("/dev/null", "w"), preexec_fn=setpgrp)

def my_open(open_what: str):
    run("/usr/bin/open", open_what)
