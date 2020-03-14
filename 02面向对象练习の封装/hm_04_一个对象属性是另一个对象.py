# 同样的道理，开发的时候需要先把用到的类先定义
# 注意哈，这里明确一下，，那些是默认有值的，那些是需要传递参数的，
class Gun:
    def __init__(self, model):
        # 1.抢的型号
        self.model = model
        # 2.子弹的数量，子弹不需要传入，需要添加！
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count

    def short(self):
        # 1.判断子弹数量
        if self.bullet_count <= 0:
            print("[%s]没有子弹了" % self.model)
            return

        # 2.发射字典，-1
        self.bullet_count -= 1

        # 3.提示发射完成
        print("[%s]突突突...[%d]" % (self.model, self.bullet_count))

class Soldier:

    # none 可以设置空对象
    def __init__(self, name):
        # 1.name
        self.name = name
        # 2. gun,新兵没有枪
        self.gun = None

    def fire(self):
        # 1.判断有没有枪
        # if self.gun == None:
        if self.gun is None:
            print("%s 没有枪" % self.name)
        # 2.高喊口号
        print("冲啊...[%s]" % self.name)
        # 3.填子弹
        self.gun.add_bullet(50)

        # 4.发射
        self.gun.short()
ak47 = Gun("ak47")
# 创建士兵
xusanduo = Soldier("许三多")
xusanduo.gun = ak47
xusanduo.fire()

# 身份运算符，判断两个对象是否是一个对象的引用
# is 与 == 区别，is是看引用，== 是看值。针对None比较的时候建议使用is