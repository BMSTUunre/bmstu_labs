#!/bin/bash

# Проверяем, задана ли переменная VAR1
if [[ -z "$VAR1" ]]; then
    echo "ERROR"
else
    # Проверяем, является ли VAR1 числом
    if [[ "$VAR1" =~ ^-?[0-9]+$ ]]; then
        # Если это число, выводим его квадрат
        result=$((VAR1 * VAR1))
        echo "$result"
    else
        # Если это не число, выводим конкатенацию
        result="${VAR1}mama${VAR1}"
        echo "$result"
    fi
fi