#!/usr/bin/python3

import random

randlist = [random.randint(1,100) for x in range (1, 1000)]

mystring = "There once was a dog named Rogerrr. He was a good boy, but his bite was worse than his bark!"


r_word_list = [ word for word in mystring.split() if "r" in word]
print(r_word_list)

numlist_seven = [ x for x in randlist if x % 7 == 0]
print(len(numlist_seven))

numlist_eight = [ x for x in randlist if x % 8 == 0]
print(len(numlist_eight))
