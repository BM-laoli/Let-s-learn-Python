# 子类拥有所有父类的方法和属性,
# 在子类中，只需要封装子类特有的属性和方法就行了
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
# 所谓的传递就是 一个接一个的链式传递
xtq = Xiaotian()
xtq.bark()
xtq.fly()
xtq.ear()

