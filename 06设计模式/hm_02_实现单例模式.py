# 这个设计思路就是只用调用一次它的初始化方法，如何记录下来，并且进行判断！

class MusicPLayer(object):
    instance = None
    def __new__(cls, *args, **kwargs):
        print('创建对象，分配空间')
        # 判断是有instance
        if cls.instance is None:
            # 没有的话就创建
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        print('初始化')


player = MusicPLayer()

player2 = MusicPLayer()

print(player)
print(player2)

