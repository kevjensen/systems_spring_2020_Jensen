#!/bin/bash

first=`date +%s`
sleep 10
second=`date +%s`

result=$((second-first))

echo $result

