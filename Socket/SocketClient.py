#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo

# socket 客户端
import socket

client = socket.socket() #定义协议类型，同时生成socket链接对象

# socket 的构造函数 def __init__(self, family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None):

client.connect(('localhost',6969)) #(IP地址或者本地，端口号)
while True:
    msg = input("Please input the message that you want to send to the server")
    if len(msg) == 0 : continue #不可以发空值 发空值会卡主
    client.send(msg.encode("utf-8")) #Python 3 中只能接受 byte类型的send 中文先要encode成UTF-8

    data = client.recv(1024) #定义 data 接受返回值 接受多少个字节 eg：1024

    print(data.decode())

client.close()
