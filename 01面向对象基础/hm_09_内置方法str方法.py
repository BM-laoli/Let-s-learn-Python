
class Cat:
    def __init__(self, new_name, nwe_age):
        # self.name = "tom"
        self.name = new_name
        self.age = nwe_age
    def eat(self):
        print("%s 爱吃鱼" % self.name)

    def drink(self):
        print("%s 在喝水" % self.name)
    def __str__(self):
        # 必须放回一个str
        return "我是小猫[%s] [%.2f]" % (self.name, self.age)


# tom是一个全局比变量
tom = Cat("tom",18)
# 省去了打点调用的繁琐操作
print(tom)
