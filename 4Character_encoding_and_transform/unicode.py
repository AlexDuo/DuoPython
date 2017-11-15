#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo

# unicode （16位）称为万国码,在这里所有的中文和英文字符都占2个字节。ASCII（8位）
# utf-8 是unicode
# de的扩展集
# python的默认字符集是unicode 所以 当我们生命一个字符串的时候我们不能使用decode只能encode
import sys
print(sys.getdefaultencoding())


s = '你好'
# 这里的s是unicode 所以只能从unicode encode成utf-8
s_to_utf = s.encode("utf-8")
# 虽然这里我们已经将unicode转换成了utf-8 但是直接输出是 bytes 类型的
print(s_to_utf)
# 我们可以将bytes重新解码成字符串，但是我们要告诉他我们这个bytes类型的编码是什么（utf-8）

# GBK编码同理可证
print(s_to_utf.decode("utf-8"))
s_to_gbk = s.encode('gbk')
print(s_to_gbk.decode('gbk'))

# 如下我们可以看出我们首先将gbk decode 成 unicode 然后再 encode 成utf-8 之后对比 utf-8的 bytes 和 转换后的 bytes 我们
# 发现是相同的
s_gbk_to_utf = s_to_gbk.decode("gbk").encode("utf-8")

print(s_gbk_to_utf,'\n',s_to_utf)
