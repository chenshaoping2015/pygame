# -*- coding:utf-8 -*-
# @Time  :2020/11/20 16:12
# @Author: stevenchen

'''
写一个Bicycle（自行车）类，有run(骑行)方法，
调用时显示骑行里程km(骑行里程为传入的数据）；
再写一个电动自行车类EBicycle,继承自Bicycle，
添加电池电量valume属性，通过传入，同时有两个方法：
fill_charge(vol)用来充电，vol为电量，
'''


# 自行车类
class Bicycle:
    def run(self, km):
        print(f"自行车一共骑行了{km}公里")


# 电动自行车类
class EBicycle(Bicycle):
    # 属性需要传参定义，可以直接放到构造函数中
    # 添加电池电量valume属性
    def __init__(self, valume):
        self.valume = valume

    # 充电的方法
    def fill_charge(self, vol):
        # 充电后的电量 = 本身的电量 + 充电的电量
        self.valume = self.valume + vol
        print(f"充了{vol}度电，现在的电量为{self.valume}度")

    # 骑行方法
    '''
    run(km)方法用于骑行，每骑行10km消耗1度电，
    当电量耗尽时调用Bicycle的run方法骑行，
    通过传入的骑行里程数，显示骑行结果
    '''

    def run(self,km):
        #获取当前电量所能电动骑行的最大里程数
        power_km = self.valume * 10

        #当前电量足够时，直接用最大的里程数
        if power_km >= km :
            print(f"使用电瓶车骑行了{km}公里")
        else:
            #当电量不够时，在电用完后，还需要用脚骑
            print(f"使用电瓶车骑行了{power_km}公里")
            #非继承调用
            # bike = Bicycle()
            # bike.run(km - power_km)
            #继承调用
            super().run(km - power_km)


a = EBicycle(10)
a.run(102)
