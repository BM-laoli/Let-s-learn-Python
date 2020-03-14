class Women:
    def __init__(self, name):
        self.name = name
        self.__age = 18

    def __secret(self):
        print("%s 的年龄是 %d" % (self.name, self.__age))

xiaofang = Women("小芳")

# 私有属性，可以通过__ 两个下划线定义，不能在外界，直接访问，但是内部可以访问
# 私有方法也是一样的，但是python没有真正意义的私用，我们也还是可以访问的 箭头
# _类名__原来的私有值
print(xiaofang._Women__age)





