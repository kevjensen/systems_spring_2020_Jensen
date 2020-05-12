#!/usr/bin/python3 

from sys import argv

print("Number of command line arguments: {0}".format(len(argv)))

print("Length of first command line argument: {0}".format(len(argv[1])))

print("Entire argv list: {0}".format(str(argv)))
