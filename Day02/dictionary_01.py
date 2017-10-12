#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo

# 字典使用{}来标识，字典使用 key-value pair 键值对,字典是

info = {
    "stu01":"Duo Zhang",
    "stu02":"Tao Yan",
    "stu03":"Guanqi Guo",
    "stu04":"Justin Wang"
}
# 存在赋值动作会修改，不存在赋值动作相当在字典中增加条目
info["stu04"] = "村头老贾"
info["stu05"] = "Shengya Zhang"
# del不是list或者dictionary的方法是Python的方法
del info["stu05"]
info.pop("stu04")#根据键值删除指定键值
# 随意删除一个
# info.popitem()
print(info)
# 如果我们任意调用一个字典中的数据，并不做任何操作，如果存在则不报错，不存在则报错 eg:
# info["stu005"]
# 对于字典，安全的获取方法是get
print(info.get("stu06"))#例如06不存在则会返回none
# 判定指定键值对是否存在存在返回true不存在返回flase
print("stu04" in info)