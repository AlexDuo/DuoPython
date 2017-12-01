#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo
user,pwd = 'duo','zd900824'
def auth(auth_type):
    # 检测auth_type是否被传进来了
    # print('the current authentication method is:%s'%auth_type)
    def outer_wrapper(func):
        def wrapper(*args,**kwargs):
            if auth_type == "local":
                username = input("please input username:").strip()# strip() 方法用于移除字符串头尾指定的字符（默认为空格）
                password = input("please input password:").strip()

                if user == username and pwd ==password:
                    print("user has passed the authentication")
                    return func(*args,**kwargs) #写return是为了接收有返回值的函数的返回值
                else:
                    exit("invalid username or password")
            elif auth_type == "remote":
                print("this means to do remote authentication")
                print("welcome to new page")
        return wrapper
    return outer_wrapper



def index():
    print('welcome to index')
@auth(auth_type = "remote")
def home():
    print('welcome to the users home')
    return "from home"
@auth(auth_type = "remote")
def bbs():
    print('welcome to bbs page')

print(home())