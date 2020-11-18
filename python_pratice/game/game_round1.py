# -*- coding:utf-8 -*-
# @Time  :2020/11/18 17:04
# @Author: stevenchen

'''
一个回合制游戏，每个角色都有hp 和 power ,hp代表血量，power代表攻击力
hp的初始值为1000，power的初始值为200，
定义一个fight方法：
my_final_hp = my_hp - enemy_power
enemy_final_hp = enemy_hp - my_power
两个hp进行对比，血量剩余多的人获胜
'''

#定义fight函数实现游戏逻辑
def fight():
    #定义四个变量存放初始数据
    my_hp = 1000
    my_power = 200
    enemy_hp = 1000
    enemy_power = 200

    #定义血量的最终计算方式
    my_final_hp = my_hp - enemy_power
    enemy_final_hp = enemy_hp - my_power

    #判断输赢
    # if my_final_hp > enemy_final_hp:
    #     print("WIN")
    # else:
    #     print("GAME OVER")

    #三目运算
    print("WIN") if my_final_hp > enemy_final_hp else print("GAME OVER")

fight()






