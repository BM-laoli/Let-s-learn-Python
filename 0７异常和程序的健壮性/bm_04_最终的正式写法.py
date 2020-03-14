
try:
    # 尝试执行的代码
    num = int(input('输入一个整数：'))

    result = 8 / num

    print(result)
except ZeroDivisionError:
    print('除０错误')
except ValueError:
    print('类型错误不能是０或者小数')

except Exception as result:
    print('未知错误：%s' % result)
else:
    # 没有异常才会执行的业务代码
    result = 8 / num
    print(result)
finally:
    # 无论有没有异常都会执行
    pass
