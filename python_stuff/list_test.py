#!/usr/bin/python3

numlist = list(range(11))

print("Print the number 4: {0}".format(numlist[4]))

print("Print the number 8: {0}".format(numlist[8]))

print("Print whole list: {0}".format(numlist))

#Pops off the last element
numlist.pop()

print("Prints the whole list after popping: {0}".format(numlist))

#Appends the number 24 to my list
numlist.append(24)

print("Print list after appending the number 24: {0}".format(numlist))

#Pops the number 4
numlist.pop(4)

print("Print after popping 4: {0}".format(numlist))

#Prints the length of the list
print("Length of list: {0}".format(len(numlist)))

