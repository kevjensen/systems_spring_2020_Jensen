#!/usr/bin/python3

from collections import Counter

class GroceryBag:
     def __init__(self):
         self.bag = {}
         self.item_name = None
         self.count = None
     def add_item(self, item_name, count):
         self.bag[item_name] = count
     def __add__(self, other_bag):
         #Cool function I learned about in a Python coding book (Python Crash Course). Just seemed very simple to implement!
         return Counter(self.bag) + Counter(other_bag.bag)
     def __sub__(self, other_bag):
         return Counter(self.bag) - Counter(other_bag.bag)

my_bag = GroceryBag()
my_bag.add_item("Bananas", 10)
my_bag.add_item("Apples", 5)
other_bag = GroceryBag()
other_bag.add_item("Bananas", 5)
other_bag.add_item("Cheerios", 6)
print(other_bag.bag)
print(my_bag.bag)

third_bag = my_bag + other_bag
print(third_bag)

fourth_bag = my_bag - other_bag
print(fourth_bag)




