#!/bin/bash

read a

for (( i=0; i<= $(( $a / 3 )); i++ )); do
    echo -n "$i "
done
