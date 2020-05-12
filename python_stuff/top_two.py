#!/usr/bin/python3

def top_two (num_list):
    top = max(num_list)
    num_list.remove(top)
    second = max(num_list)

    return top, second 

my_list = [10, 23, 66, 4, 87, 200, 0]

top, second = top_two(my_list)

print("The two highest numbers from the list are: %d and %d" % (top, second))
