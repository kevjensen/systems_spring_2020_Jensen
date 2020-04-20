#!/bin/bash

for f in $(ls);do
	count=$((count+1))
done

if [[ count > 10 ]]; then
	echo "Count is greater than 10."
elif [[ count < 10 ]]; then 
	echo "Count is less than 10."
else 
	echo "Count is equal to 10."
fi
