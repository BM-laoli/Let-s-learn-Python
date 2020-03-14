# 不推荐，对象名.类名属性可能已发的问题

class Tool(object):
    # 定义类属性，记录工具的类型
    cout = 0
    def __init__(self, name):
        self.name = name
        #类的属性+1，注意哈这里不能用self
        Tool.cout += 1

tooll = Tool("斧头")
tooll1 = Tool("榔头")
tooll2 = Tool("水桶")
tooll3 = Tool("螺丝刀")


tooll3.cout = 99
print(tooll3.cout)
# 这个陷阱在这里，python赋值意思就是，先找，找不到就是创建一个并且赋值
print('====> %d' % Tool.cout)