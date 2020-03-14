class Cat:
    def __init__(self,new_name):
        # self.name = "tom"
        self.name = new_name
    def eat(self):
        print("%s 爱吃鱼" % self.name)

    def drink(self):
        print("%s 在喝水" % self.name)
# 我们可以使用.属性，利用赋值语句可以添加属性，但是极其不推荐


tom = Cat("tom")
# tom.name = "tom"
tom.eat()
tom.drink()


lazy_cat = Cat("DALANMAO")
lazy_cat.eat()
lazy_cat.drink()

