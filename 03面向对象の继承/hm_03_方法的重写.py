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

    # 重写父类的方法,重写重写，就是重新编写类的实现细节，Overrides method in Anima
    def drink(self):
        print("哮天犬和天河的水")
    # 当父类的方法，无法满足需求的时候，我们就怎么干！

xtq = Xiaotian()
xtq.bark()
xtq.fly()
xtq.ear()

xtq.drink()

