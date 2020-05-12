#!/usr/bin/python3

input1 = input("Please enter the first number.")

operand1 = int(input1)

input2 = input("Please enter the second number (greater than {0}).".format(operand1))

operand2 = int(input2)

while operand1 > operand2:
    input2 = input("Please enter the second number (greater than {0}).".format(operand1))
    operand2 = int(input2)

sevenonly = []
fouronly = []
both = []

for x in range(operand1, operand2):
    if (x % 7 == 0):
        sevenonly.append(x)

for x in range(operand1, operand2):
    if (x % 4 == 0):
        fouronly.append(x)

for x in range(operand1, operand2):
    if (x % 4 == 0):
        both.append(x)
    if (x % 7 == 0):
        both.append(x)

#both = sevenonly + fouronly
        
print("Numbers divisible by 7: {0}".format(sevenonly))

print("Numbers divisible by 4: {0}".format(fouronly))

print("Numbers divisible by both: {0}".format(both))
