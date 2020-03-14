# 1.注意哈，被使用的类，应该先开发
class HouseItem:

    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s]占地 【%.2f】" % (self.name, self.area)


# 2.设计，房子类，注意，类和类间需要有两个空行
class House:
    def __init__(self, house_type, are):
        self.house_type = house_type
        self.are = are

        # 剩余面积
        self.free_area = are
        # 家具名称列表[] 元祖（）
        self.item_list = []

    def __str__(self):
        # 家括号，就可以实现代码换行python能够自动的江一对括号里的代码链接在一起
        return ("户型:%s \n总面积：%.2f[剩余：%.2f]\n家具:%s"
                % (self.house_type, self.are,
                   self.free_area, self.item_list))

    def add_item(self, item):
        print("要添加 %s" % item)
        # 1.判断家具面积
        if item.area > self.free_area:
            print("%s面积太大了" % item.name )
            return
        # 2.家具名称，添加到列表中
        self.item_list.append(item.name)
        # 3.计算剩余面积
        self.free_area -= item.area


bed = HouseItem("席梦思", 40)
chest = HouseItem("衣柜", 2)
table = HouseItem("插座", 60)
print(bed)
print(chest)
print(table)
print("-"*50)

# 创建房子对象
my_home = House('两室一厅', 60)
print("-"*50)
print(my_home)
print("-"*50)
my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)
print(my_home)