#!/bin/bash

sleep 30 &
pid=$!
sleep 5
kill $pid

