#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2023/12/21 20:52
# @Author  : QingYang H.
# @File    : test_plates.py
from plates import is_valid


def test_len_7():
    assert not is_valid("hhhhhhh")


def test_num_0():
    assert not is_valid("hhh01")
    assert is_valid("hhh1")
    assert not is_valid("hhh1fg")


def test_num():
    assert not is_valid("123456")


def test_02_letter():
    assert not is_valid("h23456")


def test_dun():
    assert not is_valid("...ddd")
    assert not is_valid("pyon 3")

