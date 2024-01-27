#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2023/12/27 19:54
# @Author  : QingYang H.
# @File    : test_jar.py
import pytest
from jar import Jar


def test_init():
    jar = Jar(10)
    assert jar.size == 0
    assert jar.capacity == 10
    with pytest.raises(ValueError):
        Jar(0)
    with pytest.raises(ValueError):
        Jar(-1)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(10)
    jar.deposit(1)
    assert jar.size == 1
    jar.deposit(8)
    assert jar.size == 9
    with pytest.raises(ValueError):
        jar.deposit(2)


def test_withdraw():
    jar = Jar(10)
    jar.deposit(5)
    jar.withdraw(1)
    assert jar.size == 4
    with pytest.raises(ValueError):
        jar.withdraw(5)
