#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2023/12/27 19:08
# @Author  : QingYang H.
# @File    : test_seasons.py
import pytest
from seasons import convert_date


def test_convert_date():
    assert convert_date('1991-5-15') == "Seventeen million, one hundred fifty-six thousand, one hundred sixty minutes"
    with pytest.raises(SystemExit):
        convert_date('1991.5.15')
    with pytest.raises(SystemExit):
        convert_date('cat-4')
