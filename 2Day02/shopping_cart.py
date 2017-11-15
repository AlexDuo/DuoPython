#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo


# goods = [["coffee",int(3)],["Mac Pro",int(1299)],["Iphone",int(999)],["Canon Eos-80D"],int(1100)]
# cart = []
# salary = input("please input your salary:")
# if salary.isdigit():
#     salary = int(salary)
# print(
# '''------------------------this is the list of goods-----------------------------
# 0. {list}
# ------------------------------------------------------------------------------
# '''.format(
#     list = goods.index()
# )
#       )
# item_num = input("please choose a item to purchase")
# while salary > goods[item_num][1]:
#     i = 0
#     salary = salary - goods[item_num][1]
#     cart = cart.insert(i,goods[item_num][0])
#     i +=1

# input the salary
goods = [("coffee",3),("Mac Pro",1299),("Iphone",999),("Canon Eos-80D",1100)]
cart = []
while True:
    salary = input("please input your salary:")
    if salary.isdigit():
        salary = int(salary)
        break

while True:
    for index,item in enumerate(goods):
        print(index,item)
    input_digit = input("Please input the number of product which you wish to purchase:")
    if input_digit.isdigit():
        input_digit = int(input_digit)
        if input_digit < len(goods) and input_digit >=0:
            item_price = goods[input_digit][1]
            if item_price <= salary:
                cart.append(goods[input_digit][0])
                salary -= goods[input_digit][1]
                print("Purchase success, you current balance is{balance}".format(balance = salary))
            else:
                print("Your current balance is not enough")
                break
        else:
            print("invalid option!")

    elif input_digit == "q":
        print("exit the shopping cart system")
        print("your have purchased:")
        for purchased in cart:
            print(purchased)
        break
    else:
        print("invalid option, please input a number!")