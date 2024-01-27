#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2023/12/21 21:12
# @Author  : QingYang H.
# @File    : test_fuel.py.py
import pytest
from fuel import convert, gauge


def test_fuel():
    assert convert("10/10") == 100
    with pytest.raises(ZeroDivisionError):
        assert convert("10/0")
    with pytest.raises(ValueError):
        assert convert("x/y")
        assert convert("10/9")
        assert convert('x')


def test_gauge():
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(40) == "40%"
