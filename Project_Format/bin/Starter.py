#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo

# 在bin目录下一般是程序的主启动文件，我们在这里引入全局变量，然后在这里启动各种功能

import os
import sys
# 当前文件的绝对路径
# os.path.abspath(__file__)

# 获得当前文件所述的一级目录，对于Starter.py 这个就是bin的路径  （同理返回两次我们就得到了这个project的绝对路径）
# os.path.dirname(某文件的绝对路径)

# 同理返回两次我们就得到了这个project的绝对路径,将他赋值给一个变量，这个变量就是全局环境变量
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 添加全局环境变量
sys.path.append(BASE_DIR)

# 接下来我们便可以import各种packages

from core import main

# 通过  包.方法  来调用需要使用的方法
main.printfunc('Duo')