#!/bin/bash

# Считываем значение A с клавиатуры
read A

# Проверяем, является ли A четным или нечетным
if (( A % 2 == 0 )); then
    echo "MAMA"
else
    echo "PAPA"
fi