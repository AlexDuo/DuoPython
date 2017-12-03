#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo


# json 只能处理简单的数据类型，类如字典列表，字符串 等等 json是用于不同程序之间进行数据交互
import json
import pickle


f = open('test.txt','r')
# open 了文件之后使用 json.loads来加载文件 f.read() 是读取文件
# data = json.loads(f.read())
#
#
# print(data["age"])

data = eval(f.read())

print(data['age'])