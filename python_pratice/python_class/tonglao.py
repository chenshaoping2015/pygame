# -*- coding:utf-8 -*-
# @Time  :2020/11/21 18:02
# @Author: stevenchen
'''
定义一个天山童姥类 ，类名为TongLao，
属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，
see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），
则打印，“师弟！！！！”，如果传入“李秋水”，打印“师弟是我的！”，
如果传入“丁春秋”，打印“叛徒！我杀了你”
fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。
需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。
'''


# 定义天山童姥类
class TongLao:
    def __init__(self, power):
        self.hp = 1000
        self.power = power

    # see_people方法，需要传入一个name参数
    def see_people(self, name):
        if name == "WYZ":
            print("师弟")
        elif name == "李秋水":
            print("师弟是我的！")
        elif name == "丁春秋":
            print("叛徒！我杀了你")

    # 定义fight_zms方法（天山折梅手）
    def fight_zms(self, enemy_hp, enemy_power):
        my_power = self.power * 10  # 调用时自己武力值提升10倍
        my_hp = self.hp / 2  # 调用时自己血量减少两倍

        my_hp = my_hp - enemy_power
        enemy_hp = enemy_hp - my_power

        # 进行一回合制对打
        if my_hp > enemy_hp:
            # 打印我和敌人的血量
            print(f"我的剩余血量为{my_hp}")
            print(f"敌人的剩余血量是{enemy_hp}")
            print("I WIN")
            # 满足条件就跳出循环

        else:
            print(f"我的剩余血量为{my_hp}")
            print(f"敌人的剩余血量是{enemy_hp}")
            print("GAME OVER")


class XuZhu(TongLao):
    def read(self):
        print("罪过罪过")


if __name__ == '__main__':
    tonglao = TongLao(20)
    # tonglao.see_people("WYZ")
    tonglao.fight_zms(500, 200)
    xuzu = XuZhu(100)
    xuzu.read()
