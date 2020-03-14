# 值的注意的一点就是，我们不能对初始化方法进行直接的改造，但是我们可以设置标记，修改初始化动作执行次数
class MusicPLayer(object):
    instance = None

    init_flag = False
    def __new__(cls, *args, **kwargs):

        # 判断是有instance
        if cls.instance is None:

            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):

        if MusicPLayer.init_flag:
            return
        print('初始化')

        MusicPLayer.init_flag = True


player = MusicPLayer()

player2 = MusicPLayer()

print(player)
print(player2)