#!/bin/bash

# Чтение двух чисел A и B
read A
read B

# Вычисление выражений
sum=$((A + B))
sum_with_square=$((A + B * B))
difference=$((A * A - B * B))

# Вывод результатов в одну строку через пробел
echo "$sum $sum_with_square $difference"