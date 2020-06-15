#!/usr/bin/python3

import sys

arguments = len(sys.argv)
position = 1 

usr_input = sys.stdin.readline()
sys.stdout.write(usr_input)

while arguments > position:
    write_fh = open(sys.argv[position], 'w')
    write_fh.write(usr_input)
    position =  position + 1
