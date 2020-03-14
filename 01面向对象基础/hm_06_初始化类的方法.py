class Cat:
    def __init__(self):
        print("这是一个初始化方法")
# inint方法专门用来定义一个类具有那些属性的方法
        self.name = "tomy"
# 使用类民()创建对象的时候，会调用初始化的的方法。
tom = Cat()

print(tom.name)