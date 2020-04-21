#!/bin/bash

#Verify two command arguments
if [[ $# != 2 ]] ; then
	echo "Must enter two command arguments."
	exit
fi

if [[ -d "$2" ]]; then
	echo "$2 exists."
else 
	echo "$2 does not exist."
	exit
fi

#Declare and initialize variables
count=0
bytes=0
byte_total=0

for line in $(find ./ -name "*.sh");do
	#number of files
	count=$((count + 1))
	#size of files
	size=$(echo $( stat -t $line ) | cut -d " " -f 2)
	echo $size
	bytes[$count]=$size
	bytes=$((bytes + size))
	byte_total=$((byte_total + size))
	echo "bytes is: $bytes"
done

echo "Found $count $1 files under directory $2 total bytes: $byte_total"

