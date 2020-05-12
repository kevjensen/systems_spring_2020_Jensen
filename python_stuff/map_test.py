#!/usr/bin/python3

mylist = [5,6,7]

print(list(map(lambda x: [*range(x,0,-1)], mylist)))
