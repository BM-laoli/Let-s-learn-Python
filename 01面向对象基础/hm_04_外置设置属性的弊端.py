class Cat:
    def eat(self):
        print("%s 爱吃鱼" % self.name)

    def drink(self):
        print("%s 在喝水" % self.name)
# 我们可以使用.属性，利用赋值语句可以添加属性，但是极其不推荐


tom = Cat()
# tom.name = "tom"
tom.eat()
tom.drink()

# 如果运行的时候，找不到属性就会报错，对象的内部属性，都应该全部定义在类中
tom.name = "tom"

lazy_cat = Cat()
lazy_cat.name = "大懒猫"
lazy_cat.eat()
lazy_cat.drink()