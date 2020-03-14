# 多个继承，可以使子类，同事具有多个父类的方法和属性

class A:
    def test(self):
        pass

class B:
    def demo(self):
        pass

# 如何使用多继承？你只需点击搞一下就行了，括号里家父类名字
class C(A,B):
    def test1(self):
        pass

# 注意啊，在开发的时候，如果父类之间有同名的方法或者属性，的时候你就要小心的使用了，
# 避免发生混淆
