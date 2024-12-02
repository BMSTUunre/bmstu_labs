#!/bin/bash

if [[ $# -lt 1 ]]; then
    echo "ERROR"
    exit 1
fi

sum=0

for i in "$@"; do
    if [[ $i =~ ^[-|+]?[0-9]+$ ]]; then
        sum=$(( $sum + $i ))
    else
        echo "ERROR"
        exit 1
    fi
done

echo $sum
