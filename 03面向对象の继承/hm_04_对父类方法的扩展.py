
# 所谓的方法扩展，指的就是把父类的方法，变成子类某个方法的实现，的一部分
class Animal:
    def ear(self):
        print("吃---")

    def drink(self):
        print("喝---")

    def run(self):
        print("跑---")

    def sleep(self):
        print("睡---")


class Dog(Animal):
    def bark(self):
        print("wa!")

class Xiaotian(Dog):
    def fly(self):
        print("i cant fly")

    def drink(self):

    # 1.如何扩展？写子类特有的需求
        print("hehehehe")
    # 2.调用super()对象,注意哈，这里的这super是所有的父类
        super().drink()
    # 3。添加其他
    print("#$$@&(&(#&($(")

xtq = Xiaotian()

# 2.0中是不兼容spuer的。解决方法：父类名.方法(self)就行