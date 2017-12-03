#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo
import pickle

def greeting(name):
    print("hi %s"%name)

info = {
    'name' : 'Duo Zhang',
    'age':27,
    'school':'Marquette',
    'func':greeting
}
# pickle 写进去的是 Binary 类型 二进制 所以要 用 wb  write binary
f = open('test2.txt','wb')

# pickle 的 dump 可以直接 需要写入的 （字典列表等等，读进来的文件）
# dump obj+文件名 可直接写入
pickle.dump(info,f)
# dumps 命令需要调用f.write来写入
# f.write(pickle.dumps(info))
f.close()