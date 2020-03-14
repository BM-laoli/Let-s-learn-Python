# 这个模式的目的——让类创建的对象，在系统中只有唯一的一个实例
# 每一次指向类民()放回的对象，内存地址是相同的

# __new__是一个obj老祖宗提供的一个内置方法，这个放回值是对象的引用，用来给对象实例分配内存空间
# 注意哈，这里的要重写它

class MusicPLayer(object):
    # *表示多值的元祖，＊＊多值的字典
    # ｎｅｗ会自动调用
    def __new__(cls, *args, **kwargs):
        print('创建对象，分配空间')

        # 要调用父类的方法需要指定super()对象
        insrance = super().__new__(cls)

        return insrance

    def __init__(self):
        print('初始化')


player = MusicPLayer()

player2 = MusicPLayer()

print(player)
print(player2)

