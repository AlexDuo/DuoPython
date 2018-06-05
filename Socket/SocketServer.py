#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo


import socket


server = socket.socket()

server.bind(('localhost',6969)) #服务器端绑定要监听的端口

server.listen() #进行监听 ()中可以填入数字，意为最多可以挂载的链接数
print("I am waiting for the request")

# conn就是客户端链接过来而在服务器端为其生成的一个链接实例
conn,addr = server.accept() #等待响应  客户端的请求会返回两个值 客户端具体的实例Conn，一个是地址addr
print(conn,addr)
print("I got request")

while True:

    data = conn.recv(1024)

    print("receive is %s" %data.decode())

    conn.send(data.upper())

server.close()