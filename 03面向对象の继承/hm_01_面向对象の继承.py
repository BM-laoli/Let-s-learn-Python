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

dg = Dog()
dg.run()
dg.bark()

# 专业术语：dog是animal的派生，animal是dog的基类，dog是animal的派生