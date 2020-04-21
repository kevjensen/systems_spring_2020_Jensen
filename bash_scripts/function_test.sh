#!/bin/bash
val1=$1
val2=$2
function ADD {
	#if [[ $# != "2" ]];then
	#echo "Not enough arguments."
	#exit
	#fi
	addresult=$((val1+val2))
	echo "$addresult"
}

addval=$(ADD)
echo "Addition is" $addval

function MULTIPLY {
	#if [[ $# != "2" ]];then
	#echo "Not enough arguments."
	#exit
	#fi
	multresult=$((val1*val2))
	echo "$multresult"
}

multval=$(MULTIPLY)
echo "Multiplication is" $multval


function FACTORIAL {

	if [[ "$1" -gt "1" ]];then
	echo $(($1 * $(FACTORIAL $(($1 - 1)))))
	else
		echo "1"
	fi
}

factorialval=$(FACTORIAL $1)
echo "Factorial is" $factorialval
	
