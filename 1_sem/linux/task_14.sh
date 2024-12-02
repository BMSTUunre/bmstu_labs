#!/bin/bash
sum=0

for i in "$@"; do
    sum=$(( $sum + $i ))
done

echo $sum