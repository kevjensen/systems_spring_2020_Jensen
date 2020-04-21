#!/bin/bash

sum=0

while [[ $# -gt 0 ]];do
	sum=$(echo $sum + $1 | bc)
	shift
done

echo $sum
