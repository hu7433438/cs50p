#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2023/12/17 23:51
# @Author  : QingYang H.
# @File    : extensions.py
name = input('File name: ').lower().strip()

if name.endswith('.gif'):
    print('image/gif')
elif name.endswith('.jpg') or name.endswith('.jpeg'):
    print('image/jpeg')
elif name.endswith('.png'):
    print('image/png')
elif name.endswith('.pdf'):
    print("application/pdf")
elif name.endswith('.zip'):
    print("application/zip")
elif name.endswith('.txt'):
    print('text/plain')
else:
    print('application/octet-stream')
