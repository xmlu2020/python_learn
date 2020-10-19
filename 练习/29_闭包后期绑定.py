"""
知识点：
1、列表推导式 [x for x in range(10)]
2、匿名函数 lambda 参数 : 返回值,lambda后面的参数就是函数的形参，冒号后面的表达式就是返回值。
3、闭包函数
4、for循环对函数的迭代调用
5、闭包函数的调用
https://blog.csdn.net/zhao_5352269/article/details/89175502
"""


def multi():
    return [lambda x: i*x for i in range(4)]


print([m(3) for m in multi()])


def num():
    sub = []
    for i in range(4):
        def num2(x):
            return x * i
        sub.append(num2)
    # print(sub)
    return sub
    # return [lambda x: i * x for i in range(4)]


print([m(3) for m in num()])


if __name__ == '__main__':
    multi()
    num()