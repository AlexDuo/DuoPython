#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo

# 序列化就是把内存中的内容变成字符串存储到硬盘中

import json

info = {
    'name' : 'Duo Zhang',
    'age':27,
    'school':'Marquette'
}

f = open('test.txt','w')

f.write(json.dumps(info))
# json.dumps 会将字典变成字符串
# print(json.dumps(info))

f.close()