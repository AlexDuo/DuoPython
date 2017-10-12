#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo

count = 0
age = 27

while count < 3:
    guess_age = int(input("plz input a age"))
    if guess_age < age:
        print("give me a bigger one")
    elif guess_age > age:
        print("give me a smaller one")
    else:
        print("you got it")
        break
    count +=1
    if count == 3:
        confirm = input("You have tried more than 3 times,please input Y/N to choose weather continue or not")
        if confirm != "N":
            count = 0
