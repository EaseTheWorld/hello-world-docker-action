#!/bin/sh -l

echo "Hello $1"
ls -l
time=$(date)
echo "::set-output name=time::$time"
