class Cat:
    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫在喝水")

tom = Cat()

tom.eat()
tom.drink()

lazy_cat = Cat()
lazy_cat.eat()
lazy_cat.drink()


print(tom)
print(lazy_cat)

# 还是原来的对象，都是同一只猫咪
# 使用相同的类，可以创建很多不同的对象
lazy_cat2 =lazy_cat
print(lazy_cat2)