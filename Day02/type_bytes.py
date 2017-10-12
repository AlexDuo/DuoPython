#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo

# 在Python中二进制文件都是由 bytes 存储，例如：音频，视频。Python3中不会混用str和bytes
# 所以必须清晰的使用str和bytes 而 在python中 str和bytes是可以拼接的。在Python3中字节包和字符串
# 是不能混用的

# 字符串转二进制用encode 二进制转字符串用decode

msg = 'this is a string type variable'
# 这就是转成bytes再转回utf-8 如果输出的最后结果是二进制的（bytes）前面会有一个b
print(msg.encode(encoding='utf-8').decode(encoding='utf-8'))