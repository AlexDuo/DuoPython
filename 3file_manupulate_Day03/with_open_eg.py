#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo


with open('sbchickensoup','r',encoding='utf-8') as f:
    for line in f:
        print(line)

# 同时使用with open 也可以打开多个文件

# with open('sbchickensoup','r',encoding='utf-8') as f, open('sbchickensoup2','r',encoding='utf-8') as f2:
# 因为python的规范是一行不要超过80个字符，我们也可以用如下的方式进行书写

# with open('sbchickensoup','r',encoding='utf-8') as f,\
#      open('sbchickensoup2','r',encoding='utf-8') as f2,\
#      open('sbchickensoup3','r',encoding='utf-8') as f3:
# 这样打开了几个文件便会清晰可见