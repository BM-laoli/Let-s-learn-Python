# 在一个复杂的大型程序中，所有的异常你没办法全料到

# 注意ｒｅｓｕｌｔ是一个变量名，里面存的就是具体捕获到的异常，这个ｒｕｅｌ不一定非要这个名字

try:
    num = int(input('输入一个整数：'))

    result = 8 / num

    print(result)
except Exception as result:
    print('未知错误　%s ' % result)
except ValueError:
    print('类型错误不能是０或者小数')

#　经验：在开发的时候，如果我们能处理一些异常就处理，最后那些不可预测的异常就来一个Exception就好了