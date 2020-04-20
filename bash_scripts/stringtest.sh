#!/bin/bash

if [[ $# != 2 ]] ; then
	echo "Must enter two command arguments."
fi
if [[ $1 == $2 ]] ; then 
	echo "Strings are the same."
elif [[ $1 < $2 ]] ; then 
	echo "String" $1 "comes before" $2"."
elif [[ $1 > $2 ]] ; then
	echo "String" $2 "comes before" $1"."
fi
