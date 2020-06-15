#!/usr/bin/python3

import json
from functools import reduce
import pprint as pp

billy_avg_grade = 0

total = float(0)
count = 0
with open('grades.json') as json_fh:
    grade_data = json.load(json_fh)
    for student in grade_data['students']:
        print(student['grades'])
        for assn in student['grades']:
           for key in assn:
               print("key {0}, assn {1}".format(key, assn[key]))
               total += assn[key]
               count = count + 1
        avg = total / count
        assn['average'] = avg
        print(student['grades'])
    with open('grades_with_avg.json', 'w') as json_wh:
        json.dump(grade_data, json_wh)        



