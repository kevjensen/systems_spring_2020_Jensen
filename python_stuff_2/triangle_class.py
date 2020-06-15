#!/usr/bin/python3

import math

class Triangle:

    #Ctor
    #Takes three parameters; length of the sides and length of the base
    #Ensure the base is less than the sum of the two sides (print an error)
    def __init__ (self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        if self.side_c > (self.side_a + self.side_b):
            print("Error: invalid base and side inputs")

    #Member function to return the perimeter of the triangle
    def perimeter(self):
        perimeter = self.side_a + self.side_b + self.side_c
        return perimeter
    #Height function to return the height of the triangle
    def height(self):
        height = 2*self.area()/self.side_c
        return height
    #Function to return the area of the triangle
    def area(self):
        area = math.sqrt(self.perimeter()/2*(self.perimeter()/2-self.side_a)*(self.perimeter()/2-self.side_b)*(self.perimeter()/2-self.side_c))
        return area

    #print_details function to print the perimeter, height, and area. I arbitrarily decided on a floating number to the thousandths place. I don't know why.
    def print_details(self):
        print("The area of the triangle equals: %.3f\nThe perimeter of the triangle equals: %d\nThe height of the triangle equals: %.3f" % (my_triangle.area(), my_triangle.perimeter(), my_triangle.height()))
        

user_answer = "Y"

while user_answer == "Y":

    side_1 = input("Please enter the size of triangle side a.\n")
    side_2 = input("Please enter the size of triangle side b.\n")
    side_3 = input("Please enter the size of triangle base.\n")

    side_a = int(side_1)
    side_b = int(side_2)
    side_c = int(side_3)

    my_triangle = Triangle(side_a, side_b, side_c)
    my_triangle.print_details()

    user_answer = input("Would you like to try another triangle? Y/N\n")
 
