# -*- coding:utf-8 -*-
# @Time  :2020/11/20 17:46
# @Author: stevenchen

class Game:

    def __init__(self,my_hp,enemy_hp):
        self.my_hp = my_hp
        self.my_power  = 200
        self.enemy_hp = enemy_hp
        self.enemy_power = 200

    def fight(self):
        # 加入循环，让游戏可以进行多轮
        while True:
            self.my_hp = self.my_hp - self.enemy_power
            self.enemy_hp = self.enemy_hp - self.my_power

            # 判断谁的血量小于等于0
            if self.enemy_hp <= 0:
                # 打印我和敌人的血量
                print(f"我的剩余血量为{self.my_hp}")
                print(f"敌人的剩余血量是{self.enemy_hp}")
                print("I WIN")
                # 满足条件就跳出循环
                break
            elif self.my_hp <= 0:
                print(f"我的剩余血量为{self.my_hp}")
                print(f"敌人的剩余血量是{self.enemy_hp}")
                print("GAME OVER")
                break
'''
新建一个后裔类，继承Game的hp和power,并多了护甲属性，
重新定义一个defense属性，
final_hp = hp + defense - enemy_power
enemy_final_hp = enemy_hp - power
两个hp进行对比，血量先为0的人输掉比赛
'''

class HouYi(Game):
    #定义护甲属性
    def __init__(self,defense,my_hp,enemy_hp):
        self.defense = defense
        #通过继承调用父类的构造函数，拿到父类的属性
        super().__init__(my_hp,enemy_hp)

    #改造fight方法
    def fight(self):
        # 加入循环，让游戏可以进行多轮
        while True:
            self.my_hp = self.my_hp + self.defense - self.enemy_power
            self.enemy_hp = self.enemy_hp - self.my_power

            # 判断谁的血量小于等于0
            if self.enemy_hp <= 0:
                # 打印我和敌人的血量
                print(f"我的剩余血量为{self.my_hp}")
                print(f"敌人的剩余血量是{self.enemy_hp}")
                print("I WIN")
                # 满足条件就跳出循环
                break
            elif self.my_hp <= 0:
                print(f"我的剩余血量为{self.my_hp}")
                print(f"敌人的剩余血量是{self.enemy_hp}")
                print("GAME OVER")
                break



game = HouYi(100,1000,1000)
game.fight()