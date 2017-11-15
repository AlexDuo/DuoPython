#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo
# 如何书写密文密码
# 引入Python标准库 “getpass”
import getpass
_username = 'duozhang'
_password = '123'
username = input("username:")
password = input("password:")
# getpass 在Pycharm中无法执行 可以在CMD 中执行
if _username == username and _password ==password:
    print("welcome user: {0} login..".format(username))
else:
    print("invalid username or password")


print(username,password)

