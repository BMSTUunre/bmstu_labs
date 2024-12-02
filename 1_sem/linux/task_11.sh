#!/bin/bash

read a

for (( i=0; i< $(( $a / 2 )); i++ )); do
    echo $i
done