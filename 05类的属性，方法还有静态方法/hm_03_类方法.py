
# 实例方法的第一个参数必须是self那个对象调用他，他就是那个对象的引用，
# 类方法的第一个值是cls，那个类调用他，他就是那个类的引用
class Tool(object):
    # 定义类属性，记录工具的类型
    cout = 0
    # 语法结构和实例方法一样
    @classmethod
    def show_tool_count(cls):
        print("====> %d" % cls.cout)

    def __init__(self, name):
        self.name = name
        #类的属性+1，注意哈这里不能用self
        Tool.cout += 1



tooll = Tool("斧头")
tooll1 = Tool("榔头")
tooll2 = Tool("水桶")
# tooll3 = Tool("螺丝刀")


# print(Tool.show_tool_count())
Tool.show_tool_count()