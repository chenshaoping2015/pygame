# -*- coding:utf-8 -*-
# @Time  :2020/11/18 17:21
# @Author: stevenchen

#定义fight函数实现游戏逻辑
def fight():
    #定义四个变量存放初始数据
    my_hp = 1000
    my_power = 200
    enemy_hp = 1000
    enemy_power = 199

    #加入循环，让游戏可以进行多轮
    while True:
        my_hp = my_hp - enemy_power
        enemy_hp = enemy_hp - my_power

        #判断谁的血量小于等于0
        if enemy_hp <=0:
            print("I WIN")
            #满足条件就跳出循环
            break
        elif my_hp <=0:
            print("GAME OVER")
            break

fight()

