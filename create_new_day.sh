#!/usr/bin/env bash

set -ex

if [ -z "${1+x}" ]; then
    read -rp "Enter the day number: " -s day
else
    day=$1
fi

dirname="advent_of_code/day_${day}"

if [ ! -d "$dirname" ]; then
    echo "Creating directory ${dirname}"
    mkdir "$dirname"
    touch "$dirname/__init__.py"
    touch "$dirname/input.txt"
    touch "$dirname/part_1.py"
    touch "$dirname/part_2.py"
    touch "$dirname/test_day_${day}.py"
fi