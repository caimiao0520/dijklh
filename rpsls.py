#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：
日期：
"""

import random



# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀


def name_to_number(name):# 显示用户输入提示，用户通过键盘将自己的游戏选择对象输入，存入变量player_choice
    if name == "石头":
        number = 0
    elif name == "史波克":
        number = 1
    elif name == "纸":
        number = 2
    elif name == "蜥蜴":
        number = 3
    else:
        number = 4
    return number

    # 使用if/elif/else语句将各游戏对象对应到不同的整数


def number_to_name(number):# 调用name_to_number()函数将用户的游戏选择对象转换为相应的整数，存入变量player_choice_number
    if number == 0:
        name = "石头"
    elif number == 1:
        name = "史波克"
    elif number == 2:
        name = "纸"
    elif number == 3:
        name = "蜥蜴"
    else:
        name = "剪刀"
    return name


import random


def rpsls(player_choice):
    print("您的选择是",player_choice)
    player_number=name_to_number(player_choice)
    comp_number=random.randrange(0,5)# 调用number_to_name()函数将计算机产生的随机数转换为对应的游戏对象
    com_choice=number_to_name(comp_number)
    print("计算机的选择为:%s" % com_choice)
    difference = (player_number-comp_number) % 5# 利用if/elif/else 语句，根据RPSLS规则对用户选择和计算机选择进行判断，并在屏幕上显示判断结果
    if difference == 1 or difference == 2:
        print("您赢了")
    elif difference == 3 or difference == 4:
        print("计算机赢了")
    else:
        print("您和计算机出的一样呢")


# 对程序进行测试
print("欢迎使用RPSLS游戏")
print("游戏规则为：剪刀能剪纸和蜥蜴；纸可以包住石头，驳斥Spock；石头击烂蜥蜴和剪刀；蜥蜴可以毒害Spock，吃纸；Spock可以砸碎剪刀，使石头蒸发")
print("----------------")
print("请输入您的选择:")
choice=input()
rpsls(choice)


