#!/usr/bin/env python3
# -*- coding: utf-8 -*-
for i in range(100, 999):
   a = i//100
   b = i % 10
   c = i % 100
   d = c//10
   s = a+b+d
   if s % 7 == 0 and i % 7 == 0:
    n =+ i
print(n,"Всего чисел")