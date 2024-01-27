#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 1/11/2024 3:56 PM
# @Author  : QingYang H.
# @File    : project.py
import json
import socket
import sys
import threading

import enums
import utils

is_running = True


def send_msg(s: socket.socket, prompt, msg_type=3):
    try:
        s.send(utils.gen_message(msg_type, prompt))
    except socket.error:
        print("Unable to connect")
        s.close()


def recv_msg(s: socket.socket):
    try:
        packets = s.recv(enums.BUF_SIZE)
        if len(packets) == 0:
            s.close()
            global is_running
            is_running = False
            return
        message = json.loads(packets)
        if message['code'] != 0:
            print(message)
        return message
    except socket.error:
        print("Unable to recv")


def send_and_recv(s: socket.socket, action, msg_type):
    try:
        send_msg(s, input(action), msg_type)
    except EOFError:
        s.close()
        sys.exit("Ctrl D!")
    return recv_msg(s)


def send_need_code0(s: socket.socket, message_str, msg_type):
    msg = send_and_recv(s, message_str, msg_type)
    while msg.get('code') != 0:
        msg = send_and_recv(s, message_str, msg_type)


def recv_forever(s: socket.socket):
    while is_running:
        message = recv_msg(s)
        if message:
            print(message.get('message'))


def send_forever(s: socket.socket):
    global is_running
    while is_running:
        try:
            send_msg(s, input())
        except (EOFError, UnicodeDecodeError):
            print("Ctrl D!")
            s.close()
            is_running = False


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((enums.HOST, enums.PORT))
    except ConnectionRefusedError:
        sys.exit("Connection refused!")
    send_need_code0(client_socket, 'your nickname: ', 1)
    send_need_code0(client_socket, 'Room and password: ', 2)

    t1 = threading.Thread(target=send_forever, args=(client_socket,))
    t1.start()
    t2 = threading.Thread(target=recv_forever, args=(client_socket,))
    t2.start()
    t2.join()
    t1.join()
    client_socket.close()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit("Ctrl+C pressed. Bye!")
