# 错误／异常有种类

# 需求：输入一个数字，让他去８去除法运算,处理不同的代码
# 关于到底是什么的错误，控制台最后一行提示的第一个信息就是
try:
    num = int(input('输入一个整数：'))

    result = 8 / num

    print(result)
except ZeroDivisionError:
    print('除０错误')
except ValueError:
    print('类型错误不能是０或者小数')
