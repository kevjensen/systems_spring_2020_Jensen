#!/usr/bin/python3

import csv
import sys

csv_items = []
with open("pretend_data.csv") as csv_in:
    my_reader = csv.DictReader(csv_in, fieldnames=['Name', 'Grade'], delimiter=",")
    for row in my_reader:
        csv_items.append(row)
    
print(csv_items)

with open("pretend_data.psv", 'w') as psv_out:
    my_writer = csv.DictWriter(psv_out, fieldnames=['Name','Grade'], delimiter="|", quotechar="'")
    my_writer.writeheader()
    for item in csv_items:
        my_writer.writerow(item)
