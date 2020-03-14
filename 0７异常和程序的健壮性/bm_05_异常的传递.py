def demo01():
    return int(input('输入整数'))


def demo2():
    return  demo01()

try:
    print(demo2())
except Exception as ser:
    print('未知错误　%s' % ser)
# 在程序中，如果出现了异常，会一级一级的向上传递


# 这样以来我们就不必，一个函数一个函数的去捕获异常来了，统一的在主程序中，统一的捕获异常
