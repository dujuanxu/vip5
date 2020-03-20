
# Python练习题：
# 1、打印小猫爱吃鱼，小猫要喝水
class Animal(object):
    def eat(self, food):
        print("------吃", food)

    def drink(self, d):
        print("......喝", d)


class Cat(Animal):

    def eat(self, food):
        print("小猫爱吃", food)

    def drink(self, d):
        print("小猫要喝", d)

def test_cat():
    c = Cat()
    c.eat('鱼')
    c.drink('水')

# 2、小明爱跑步，爱吃东西。
# 1）小明体重75.0公斤
# 2）每次跑步会减肥0.5公斤
# 3）每次吃东西体重会增加1公斤
# 4）小美的体重是45.0公斤


class Person2(object):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def run(self):
        self.weight -= 0.5
        print("%s 体重是 %f" % (self.name, self.weight))

    def eat(self):
        self.weight += 1
        print("%s 体重是 %f" % (self.name, self.weight))


def test_run_eat():
    xming = Person2('小明',75)
    xmei = Person2('小美', 45)
    xmei.eat()
    xmei.eat()
    xming.run()
    xmei.run()


# 3、摆放家具
# 需求：
# 1）.房子有户型，总面积和家具名称列表
#    新房子没有任何的家具
# 2）.家具有名字和占地面积，其中
#    床：占4平米
#    衣柜：占2平面
#    餐桌：占1.5平米
# 3）.将以上三件家具添加到房子中
# 4）.打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表


class House(object):

    def __init__(self, housetype, area):
        self.housetype = housetype
        self.area = area
        self.area_free = area
        self.furniture = []

    def info(self):
        print('户型:%s 总面积:%f 剩余面积:%f '%(self.housetype, self.area,self.area_free))

        if len(self.furniture) > 0:
            print('家具列表为：')
            for fur in self.furniture:
                print(fur.name, '面积：', fur.area)
        else:
            print("目前没有家具")

    def add_furniture(self, fur):
        self.furniture.append(fur)
        self.area_free -= fur.area
        print("添加一件家具:", fur.name)


class Furniture(object):

    def __init__(self, name, area):
        self.name = name
        self.area = area


def test_house():
    h = House('三室一厅', 120)
    h.info()
    bed = Furniture('床', 4)
    cupboard = Furniture('衣柜', 2)
    table = Furniture('餐桌', 1.5)
    h.add_furniture(bed)
    h.info()
    h.add_furniture(cupboard)
    h.info()
    h.add_furniture(table)
    h.info()


# 4.士兵开枪
# 需求：
# 1）.士兵瑞恩有一把AK47
# 2）.士兵可以开火(士兵开火扣动的是扳机)
# 3）.枪 能够 发射子弹(把子弹发射出去)
# 4）.枪 能够 装填子弹 --增加子弹的数量

class Gun(object):

    def __init__(self, gun_type, capacity, bullet_num = 0):
        self.bullet_num = bullet_num    # 已装子弹数
        self.gun_type = gun_type        # 手枪型号
        self.capacity = capacity        # 弹匣容量

    def is_full(self):
        if self.bullet_num == self.capacity:
            return True
        else:
            return False

    def is_empty(self):
        if self.bullet_num == 0:
            return True
        else:
            return False

    def shoot(self):
        if not self.is_empty():
            print("shoot==============")
            self.bullet_num -= 1
        else:
            print("cant't  shoot========,bullet is out=====")

    def load(self):
        if not self.is_full():
            self.bullet_num += 1
            return True
        else:
            print("can't add bullet======, bullet is full")


class Soldier(object):

    def __init__(self, name, gun):
        self.name = name
        self.gun = gun

    def pull(self):
        self.gun.shoot()


def test_soldier():
    g = Gun('AK47', 30)

    s = Soldier('Ryan', g)
    g.load()
    g.load()
    s.pull()
    s.pull()
    s.pull()

if __name__ == '__main__':
    test_soldier()