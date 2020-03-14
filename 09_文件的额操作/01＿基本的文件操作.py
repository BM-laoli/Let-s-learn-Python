# 在计算机中操作文件三大步奏
# １．　打开文件＼
# ２．修改文件（）写　读
# ３．关闭文件
#
# 在ｐｙｔｈｏｎ中操作文件要使用一个函数还有三个方法
#
# １．open 返回文件操作对象
# read write close

# 目前的需求打开文件并且显示在控制台
# 先看一下如何读取
file = open('dasd.txt')
text = file.read()
print(text)
file.close()
# 我们来讲一个概念　文件对象的读取操作里面存在一个文件指针　
# 读一起之后就会移动到末尾．red只能调用一次

# 我们来看一下　打开文件的第二参数 默认的 r 除此之外　ｗ a    r+ w+ a+

file2 = open('dasd.txt',"w")
file2.write('这个是写如的文件')
file2.close()


# 除了ｒｅｄ之后我们还有一个读取一行的操作　readline 是一个高效的读取操作

file3 = open("dasd.txt")

while True:
    text2 = file3.readline()

    if not text2:
        break

    print(text2)

# 注意哈我们这里有是循环去打印文件内容
file3.close()

