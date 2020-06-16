#!/usr/bin/python3

from functools import reduce

class Shape:
    def __init__(self, num_sides, side_lengths=[]):
        self.num_sides = num_sides
        self.side_lengths = side_lengths
    def perimeter(self):
        return reduce(lambda x, y: x + y, self.side_lengths)
    def area(self):
        return "Function not implemented."
    def get_name(self):
        return "Shape"
    def print_shape_detail(self):
        print("This {0} has {1} sides, a perimeter of {2}, and an area of {3}".format(self.get_name(), self.num_sides, self.perimeter(), self.area()))
    
class Rectangle(Shape):
    def __init__(self, side_length, width_length, num_sides=4):
        super(Square, self).__init__()
        self.side_lengths = [side_length * 2, width_length * 2]
        self.width_length = width_length
        self.side_length = side_length
        self.num_sides = num_sides
    def area(self):
        return self.side_length * self.width_length
    def get_name(self):
        return "Rectangle"

class Square(Rectangle):
    def __init__(self):
        super(Square, self).__init__()
        self.side_length = side_length
        self.num_sides = num_sides
    #def area(self):
        #return self.side_length * self.side_length
    def get_name(self):
        return "Square"



my_square = Square(2, 2)
my_rectangle = Rectangle(1, 2)
#print(my_square.print_shape_detail())
print(my_rectangle.print_shape_detail())
