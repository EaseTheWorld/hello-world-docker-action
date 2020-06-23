#!/bin/sh -l

echo "Hello $1"
ls -l
time=$(date)
echo "add $time" >> test.sh
echo "::set-output name=time::$time"
