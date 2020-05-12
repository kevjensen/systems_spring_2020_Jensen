#!/usr/bin/python3

from functools import reduce

mylist = [3,6,9,12]

def multiply_numbers(x, y):
    print("x is {0}, y is {1}".format(x, y))
    return x * y

result = reduce(multiply_numbers, mylist)
print(result)

print(reduce(lambda x,y: x * y, mylist))
