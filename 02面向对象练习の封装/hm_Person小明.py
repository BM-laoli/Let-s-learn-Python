class Persion:

    def __init__(self, name, weight):
        # 复习一下我们的属性self的传递
        self.name = name
        self.weight = weight

    def __str__(self):
        # 必须放回一个str
        return "我的名字是[%s]，有[%.2f]斤" % (self.name, self.weight)

    def ear(self):
        print("%s 是吃货" % self.name)
        self.weight += 1

    def run(self):
        print("%s 爱跑步" % self.name)
        self.weight -= 0.5


xiaoming = Persion("小明", 75.0)


xiaoming.run()
xiaoming.ear()

print(xiaoming)
