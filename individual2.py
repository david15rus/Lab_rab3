#!/usr/bin/env python3
# -*- coding: utf-8 -*-
A1 = float(input("Введите A1 "))
B1 = float(input("Введите B1 "))
C1 = float(input("Введите C1 "))
A2 = float(input("Введите A2 "))
B2 = float(input("Введите B2 "))
C2 = float(input("Введите C2 "))
if (A1 == 0 and B1 == 0) or (A2 == 0 and B2 == 0):
    print("Это не прямые")
elif A1*B2 == A2*B1 and A1*C2 == A2*C1:
    print("Прямые совпадают")
elif A1*B2==A2*B1:
    print("Прямые параллельны")
else:
    X = (C1*B2-C2*B1)/(B1*A2-B2*A1)
    Y = (C2*A1-C1*A2)/(B1*A2-B2*A1)
    print("Координата по оси OX=",X,"по оси OY=",Y)