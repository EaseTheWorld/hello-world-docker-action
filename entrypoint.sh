#!/bin/sh -l

echo "Hello $1"
ls -l
time=$(date)
echo "add $time" >> test.sh
echo "::set-output name=time::$time"
pip show Google-Search-API
python3 forgot-to-link.py README.md README.md.url
mv README.md.url README.md
