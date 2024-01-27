#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2023/12/26 18:02
# @Author  : QingYang H.
# @File    : test_um.py
from um import count


def test_count():
    assert count("um") == 1
    assert count("um, world") == 1
    assert count("hello, um, world") == 1
    assert count("hello, um") == 1


def test_upper():
    assert count("Um") == 1
    assert count("Um, world") == 1
    assert count("hello, Um, world, UM") == 2
    assert count("hello, uM, , um...") == 2


def test_word():
    assert count("yUm") == 0
