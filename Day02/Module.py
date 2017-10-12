#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo

# 模块又叫做库，库可以分为标准库和第三方库，标准库是Python自带的
# 引入了sys功能
import sys
import os
# 打印sys会输出一些列的路径。这边是环境变量
# print(sys.path)
# print(sys.argv[2])
# 这里面 cmd_result 变量里面存储的并不是查询结果，而是命令执行成功与否的代号
# cmd_result = os.system("dir")#os.system只执行命令不保存结果
cmd_result2 = os.popen("dir").read() #不适用read方法则输出的是一条内存，使用Read方法后输出的才是你存储的执行命令后得到的结果
print("-->",cmd_result2)
# 创建一个目录
os.mkdir("new_dir")
# Python 是有第三方模块的，我们也可以自己书写第三方模块
