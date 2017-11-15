#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo
# While 循环

# while 后面接条件
duo_age = 27
count = 0
while True:
    if count == 3:
        print("3 times already, you lose")
        break
    guess_age = int(input("Plz tell me the name of duo:"))
    if guess_age > duo_age:
        print("give me a smaller one:")
    elif guess_age < duo_age:
        print("give me a smaller one:")
    else:
        print("that's right!")
        break
    #     += 1 是自加运算
    count +=1