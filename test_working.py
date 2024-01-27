#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2023/12/26 17:24
# @Author  : QingYang H.
# @File    : test_working.py
from working import convert
import pytest


def test_format():
    with pytest.raises(ValueError):
        convert('9 AM - 5 PM')
    with pytest.raises(ValueError):
        convert('9AM - 5PM')
    with pytest.raises(ValueError):
        convert('09:00 AM - 17:00 PM')
    with pytest.raises(ValueError):
        convert('9:00AM to 17:00PM')


def test_convert():
    assert convert('10 PM to 8 AM') == '22:00 to 08:00'
    assert convert('10:30 PM to 8:50 AM') == '22:30 to 08:50'


def test_range():
    with pytest.raises(ValueError):
        convert('09:00 AM to 17:00 PM')
    with pytest.raises(ValueError):
        convert('19:60 AM to 5:60 PM')
    with pytest.raises(ValueError):
        convert('cat')
    with pytest.raises(ValueError):
        assert convert('09:00 AM')
