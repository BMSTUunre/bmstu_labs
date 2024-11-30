#!/bin/bash
read a
read b

for (( i=0; i<$b; i++ )); do
    echo $a
done