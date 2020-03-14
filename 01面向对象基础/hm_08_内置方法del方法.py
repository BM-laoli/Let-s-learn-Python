# 当一个对象，内存中销毁的时候，会调用一个__del__方法：
class Cat:
    def __init__(self, new_name):
        self.name = new_name
        print("%s 来了" % self.name)

    def __del__(self):
        print("%s 我去了" % self.name)

# tom是一个全局比变量
tom = Cat("tom")

# del关键字会自动删除对象
del tom
print("-" * 50)

