#!/bin/bash

data=$1
delimiter=$2
column=$3

count=0
gradesum=0
lowestgrade=1000
highestgrade=0
lownamevar=
highnamevar=
gradeavg=0

infile=$data

for line in $(cat $1);do
	#Keep track of count; num of students in class
	count=$(( count + 1))
	#Find highest grade numeric value
	if [[ $line -gt $highestgrade ]];then
		highestgrade=$(echo $line | cut -d $delimiter -f $3)
		#Find highest grade name value
		highnamevar=$(echo $line | cut -d $delimiter -f 1)
	fi
	#Find lowest grade numeric value
	if [[ $line -lt $lowestgrade ]];then
		lowestgrade=$(echo $line | cut -d $delimiter -f $3)
		#Save lowest grade name value
		lownamevar=$(echo $line | cut -d $delimiter -f 1)
	fi
	#Find total value of class grades
	x=$(echo $line | cut -d $delimiter -f $3)
	gradesum=$((gradesum + x))
done

#Find average class grade
gradeavg=$(echo $gradesum/$count | bc)	

echo "Total number of students:" $count
echo "Highest grade value:" $highestgrade
echo "Highest name value:" $highnamevar
echo "Lowest grade value:" $lowestgrade
echo "Lowest name value:" $lownamevar
echo "Average grade of class:" $gradeavg
