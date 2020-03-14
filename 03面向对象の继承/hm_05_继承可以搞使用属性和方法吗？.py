# 注意哈这里是不能的哈！，一句话就是老爸的钱包，你不动！

class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200
    def __test(self):
        print("这是我的方法 %d %d " % (self.num1, self.__num2))

    def tes(self):
        print("私用的 %d " % self.__num2)
        self.__test()
class B(A):
    pass

b = B()
b.tes()
print(b)


# 硬要弄怎么办呢？,通过媒介～
# 子类对象，可以通过父类的公用属性，访问到它的私有方法和私有属性
