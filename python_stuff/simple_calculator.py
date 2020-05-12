#!/usr/bin/python3

#Initialize response and count
response = "Y"
count = 0

#While loop so the user can process multiple computations
while response == "Y":

    input1 = input("Please enter your first operand.")

    input2 = input("Plese enter your second operand.")

    operator = input("Please enter your operator (+,-,*,/).")

    operand1 = int(input1)

    operand2 = int(input2)

#If statement computes the operation: I used the 4 space standard for indentation
    if operator == "+":
        print("Sum = {0}".format(operand1 + operand2))
    elif operator == "*":
        print("Product = {0}".format(operand1 * operand2))
    elif operator == "/":
        print("Quotient = {0}".format(operand1 / operand2))
    elif operator == "-":
        print("Difference = {0}".format(operand1 - operand2))
    else:
        print("Error: Invalid operator entry.")
    count = count + 1
    if count > 5:
        print("This seems like an excessive amount of calculations for this program.")
    response = input("Would you like to perform another calculation (Y/N)")
    

