#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2023/12/17 23:17
# @Author  : QingYang H.
# @File    : deep.py
answer = input('What is the Answer to the Great Question of Life, the Universe, and Everything?')
match answer.lower().strip():
    case '42' | '42 ' | 'forty-two' | 'forty two':
        print('Yes')
    case _:
        print('No')
