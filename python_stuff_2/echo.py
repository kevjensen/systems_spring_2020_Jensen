#!/usr/bin/python3

import sys

usr_input = None
while usr_input != "quit\n":
    usr_input = sys.stdin.readline()
    if usr_input == "quit\n":
        break 
    sys.stdout.write(usr_input)
    sys.stderr.write(usr_input)
