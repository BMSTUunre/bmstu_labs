#!/bin/bash

# Проверяем, заданы ли переменные VAR1, VAR2 и VAR3
if [[ -z "$VAR1" || -z "$VAR2" || -z "$VAR3" ]]; then
    echo "ERROR"
else
    # Приводим VAR1 к нижнему регистру для сравнения
    if [[ "${VAR1,,}" == "yes" ]]; then
        # Если VAR1 равно "yes", выводим VAR2 + VAR3
        result="$((VAR2 + VAR3))"
        echo "$result"
    else
        # В противном случае выводим VAR3 + VAR2 + VAR2
        result="$((VAR3 + VAR2 + VAR2))"
        echo "$result"
    fi
fi