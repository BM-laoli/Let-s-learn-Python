# 你需要注意的是：定义类图很重要！！


class Cat:
    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫在喝水")

tom = Cat()

tom.eat()
tom.drink()

print(tom)
addr = id(tom)
print("%d" % addr)
print("%x" % addr)

# //%d可以转化为10进位制，X表示16进制
# print("%d" % addr)
# print("%x" % addr)
