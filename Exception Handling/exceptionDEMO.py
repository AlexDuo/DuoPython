#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo

# 异常处理就是虽然程序出错了，但是我不想让用户看到，而且不想让程序崩溃

name = ['Duo Zhang','Yang chen']

dictionary = {}


try:
    # dictionary["name"]
    name[3]
except KeyError as error:
    print("there is no %s in the dictionary"%error)

except IndexError as error:
    print(error)
except Exception: #最后使用，提示未知错误。
    print("未知错误？？")

else: #没有错误的时候执行
    print("没有错误，一切正常！")

finally: #不管有没有错都会执行
    print("嗯，行，挺好，嗯……你自己加油……")