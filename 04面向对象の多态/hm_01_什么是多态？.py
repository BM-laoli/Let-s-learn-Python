# 所谓的多态，指的是。多个子类调用同一个父类的方法，但是产生不同的结果

# 前提：有继承，有重写父类中的方法

class Dog(object):
    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s 玩耍" % self.name)

class Xiaotianq(Dog):
    def game(self):
        print("%s 飞上天玩" % self.name)

class Person(object):
    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        print("%s 和 %s 快乐的玩耍" % (self.name, dog.name))
        dog.game()

# 1.创建一个狗
# wancai = Dog('旺财')
wancai = Xiaotianq('飞天旺财')
# 2.创建一个小明
xiaoming = Person('小明')
# 2.小明和狗玩
xiaoming.game_with_dog(wancai)