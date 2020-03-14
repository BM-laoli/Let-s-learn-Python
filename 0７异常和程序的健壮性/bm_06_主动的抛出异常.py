# 我们在开发的时候，对于特定的开发需求抛出异常，并且给一个处理函数去处理，比如，要求密码输入位数

# １.创建一个异常对象，用ｒａｉｓｅ关键字抛出异常对象

def input_password():

    pwd = input('输入密码：')

    # 注意哈，ｉｆ表示是如果输入是　真
    if len(pwd) >= 8:
        return pwd

    print('主动抛出异常')
    # 创建异常对象
    ex = Exception('有问题')
    raise ex
try:
    print(input_password())
except Exception as reu:
    print(reu)

# print(input_password())