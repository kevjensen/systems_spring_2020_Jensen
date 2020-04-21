#!/bin/bash

infile="alice.txt"

#Prints lines if it has the word "the" in it; unfortunately, I think this also includes words like "then"
while read line;do
	grep -i 'the'
done < $infile

#Counts the number of thes
while read line;do
	grep -o 'the' | wc -l
done < $infile


