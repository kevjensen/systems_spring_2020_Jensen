#!/usr/bin/python3

import sys

count = 0
line_number = 0
max_grade = 0
min_grade = 1000
total_grade = 0

with open("pretend_data.csv", 'r') as grades:
    for line in grades:
        count = count + 1
        line = line.strip()
        words = line.split(",")
        for word in words:
            line_number = line_number + 1
            if line_number % 2 == 0:
                total_grade = total_grade + int(word)
                if int(word) > max_grade:
                    max_grade = int(word)
                if int(word) < min_grade:
                    min_grade = int(word)

avg_grade = total_grade/count

print("Max grade: {0}\n".format(max_grade))
print("Min grade: {0}\n".format(min_grade))
print("Average grade: {0}".format(avg_grade))

with open('new_pretend_data.csv', 'w') as new_file:
    new_file.write(str(max_grade))
    new_file.write(str(min_grade))
    new_file.write(str(avg_grade))
       

