#!/usr/bin/python3

def add (operand1, operand2):
    print("{0} + {1} = {2}".format(operand1, operand2, operand1 + operand2))

def find_max (operand1, operand2):
    if (operand1 > operand2):
        return("The largest operand value is: {0}".format(operand1))
    if (operand2 > operand1):
        return("The largest operand value is: {0}".format(operand2))
    if (operand1 == operand2):
        return("The two operands are equal.")

input1 = input("Enter first operand.")
input2 = input("Enter second operand.")

in1 = int(input1)
in2 = int(input2)

add (in1, in2)
max_number = find_max (in1, in2)

print(max_number)
