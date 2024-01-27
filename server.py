#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2024/1/7 0:54
# @Author  : QingYang H.
# @File    : server.py
import asyncio
import json

import enums
import utils

users = {}
rooms = {}


async def sent_msg(writer, msg_type, message, code=0):
    writer.write(utils.gen_message(msg_type, message, code))
    await writer.drain()


def disconnect(writer):
    if writer in users:
        print(f"Connection closed by {users.get(writer)}")
        del users[writer]
        writer.close()
    for info in rooms.values():
        if writer in info['users']:
            info['users'].remove(writer)


async def handle_chat(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    while True:
        try:
            data = await reader.read(enums.BUF_SIZE)
            if len(data) == 0:
                disconnect(writer)
                break
            message = json.loads(data)
            print(f"message from {writer.get_extra_info('peername')!r}")
            match message['type']:
                case 1:
                    if message['message'] in users.values():
                        await sent_msg(writer, message['type'], "your nickname is same with others", 1001)
                    else:
                        users[writer] = message['message']
                        await sent_msg(writer, message['type'], "ok")
                case 2:
                    room_password = message['message'].split(' ', 1)
                    room = room_password[0]
                    password = room_password[1] if len(room_password) > 1 else ''
                    if room not in rooms:
                        rooms.setdefault(room, {}).setdefault('password', password)
                        rooms.setdefault(room, {}).setdefault('users', []).append(writer)
                        await sent_msg(writer, message['type'], "Create a new room")
                    elif password == rooms[room]["password"]:
                        rooms.setdefault(room, {}).setdefault('users', []).append(writer)
                        await sent_msg(writer, message['type'], "Enter room")
                    else:
                        await sent_msg(writer, message['type'], "Password error", 1002)
                case 3:
                    for info in rooms.values():
                        if writer in info['users']:
                            for user in info['users']:
                                if writer != user:
                                    await sent_msg(user, message['type'], f"{users[writer]}:\n  {message['message']}")
                                else:
                                    await sent_msg(user, message['type'], f"You:\n  {message['message']}")

            print(users, rooms, sep="\n")
        except ConnectionResetError as e:
            print(e)
            disconnect(writer)
            break


async def start():
    server = await asyncio.start_server(handle_chat, enums.HOST, enums.PORT)
    async with server:
        await server.serve_forever()


def main():
    try:
        asyncio.run(start())
    except KeyboardInterrupt:
        print("Shutting down chat server")


if __name__ == '__main__':
    main()
