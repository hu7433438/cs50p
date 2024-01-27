#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2024/1/6 22:08
# @Author  : QingYang H.
# @File    : test_project.py
import pytest

import project
import socket


def test_send_forever():
    with pytest.raises(OSError):
        project.send_forever(socket.socket(socket.AF_INET, socket.SOCK_STREAM))


def test_recv_forever():
    project.is_running = False

    assert project.recv_forever(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) is None


def test_send_need_code0():
    with pytest.raises(OSError):
        project.send_need_code0(socket.socket(socket.AF_INET, socket.SOCK_STREAM), "hu", 1)


def test_send_and_recv():
    with pytest.raises(OSError):
        project.send_and_recv(socket.socket(socket.AF_INET, socket.SOCK_STREAM), "hu", 1)


def test_recv_msg():
    assert project.recv_msg(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) is None


def test_send_msg():
    assert project.send_msg(socket.socket(socket.AF_INET, socket.SOCK_STREAM), "hu", 1) is None
