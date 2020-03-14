
class A:
    def test(self):
        pass

class B:
    def demo(self):
        pass

class C(A,B):
    def test1(self):
        pass


# 确定C类调用对象的属性,这个是一个内置属性。
# C类的MRO就是先调用C的类或者属性，然后安装MRO顺序去一个一个的找，找不到就报错
c = C()
c.test()
c.demo()
print(C.__mro__)