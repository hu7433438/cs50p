#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2023/12/26 13:06
# @Author  : QingYang H.
# @File    : test_numb3rs.py
from numb3rs import validate


def test_numb3rs():
    assert validate('1.2.3.4')
    assert validate('127.0.0.1')
    assert validate('255.255.255.255')
    assert not validate('512.1.1.1')
    assert not validate('1.512.1.1')
    assert not validate('1.1.512.1')
    assert not validate('1.1.1.512')
    assert not validate('244')
    assert not validate('255.255.255.255.1')
    assert not validate('512.512.512.512')
    assert not validate('1.2.3.1000')
    assert not validate('cat')
