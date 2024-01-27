#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2024/1/7 18:57
# @Author  : QingYang H.
# @File    : utils.py
import json


def gen_message(msg_type, message, code=0):
    # message = message if msg_type != 3 else f"{message}\n"
    return json.dumps({'type': msg_type, 'message': message, 'code': code}).encode()
