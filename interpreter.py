#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2023/12/18 0:34
# @Author  : QingYang H.
# @File    : interpreter.py
exp = input('Expression: ')
x, y, z = exp.split(' ')
if y == "+":
    print(float(x) + float(z))
elif y == "-":
    print(float(x) - float(z))
elif y == "*":
    print(float(x) * float(z))
elif y == "/":
    print(float(x) / float(z))
