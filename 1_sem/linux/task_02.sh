#!/bin/bash

# Проверяем, заданы ли переменные VAR1 и VAR2
if [[ -z "$VAR1" || -z "$VAR2" ]]; then
    echo "ERROR"
else
    # Вычисляем сумму VAR1 и VAR2
    result=$((VAR1 + VAR2))
    echo "$result"
fi