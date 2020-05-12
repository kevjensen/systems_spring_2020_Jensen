#!/usr/bin/python3

gradedict = {"Phred": 88.7774, "Aeva": 95.44443, "Ralphie": 65.0}

print(gradedict)

print("Phred's grade: {:.2f}".format(gradedict["Phred"]))

gradedict["Leon"] = 55.555

print(gradedict)
