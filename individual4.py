#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import sys
EPS = 1e-10
if __name__ == '__main__':
    x = float(input("Введите x "))
    if x == 0:
        print("Неверное значение х", file=sys.stderr)
        exit(1)
    a = x
    S, k = a, 1
    while math.fabs(a) > EPS:
        a *= (-x * (2 * k + 1) ** 2)/(4 * (k + 1) ** 2)
        S += a
        k += 1
# Вывести значение функции.
    print(f"Si({x}) = {S}")