class Cat:
    def eat(self):
        print("%s 爱吃鱼" % self.name)

    def drink(self):
        print("%s 在喝水" % self.name)
# 我们可以使用.属性，利用赋值语句可以添加属性，但是极其不推荐


tom = Cat()
tom.name = "tom"
tom.eat()
tom.drink()

lazy_cat = Cat()
lazy_cat.name = "大懒猫"
lazy_cat.eat()
lazy_cat.drink()

# self 是当前所创建对应对象的引用，方法的第一个参数永远是self