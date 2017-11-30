#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo
user,pwd = 'duo','zd900824'
def auth(func):
    def wrapper(*args,**kwargs):
        username = input("please input username:").strip()# strip() 方法用于移除字符串头尾指定的字符（默认为空格）
        password = input("please input password:").strip()

        if user == username and pwd ==password:
            print("user has passed the authentication")
            return func(*args,**kwargs) #写return是为了接收有返回值的函数的返回值
        else:
            exit("invalid username or password")
    return wrapper



def index():
    print('welcome to index')
@auth
def home():
    print('welcome to the users home')
    return "from home"
@auth
def bbs():
    print('welcome to bbs page')


index()

print(home())