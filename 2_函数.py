#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/6 21:44
# @Author  : XiaomeiLu
# @FileName: 2_函数.py
# @Software: PyCharm

'1.调用函数'
'利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：'
n1 = 255
n2 = 1000

print(hex(n1))
print(hex(n2))


'2.定义函数'
'''
定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程 ax^2+bx+c=0
计算平方根可以调用math.sqrt()函数：'''

import math


def quadratic(a,b,c):
    #math.sqrt() 计算平方根
    x1 = (-b+(math.sqrt((b**2)-4*a*c)))/(2*a)
    x2 = (-b-(math.sqrt((b**2)-4*a*c)))/(2*a)
    return x1,x2
# print("请输入a，按回车结束输入")
# x = input()
# print("请输入b，按回车结束输入")
# y = input()
# print("请输入c，按回车结束输入")
# z = input()
# p = quadratic(int(x),int(y),int(z))
# print('第一个根是',p[0])
# print('第二个根是',p[1])

print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')



'3.函数的参数'
'''以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积
 def product(x, y):
     return x * y'''


def product(x, *num):
    if len(num) > 0:
        for y in num:
            x = x * y
        return x

print(product(5))
print(product(5,6))
print(product(5,6,7))
print(product(5,6,7,9))
# 测试
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != None:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')


'4.递归函数'
'''如果一个函数在内部调用自身本身，这个函数就是递归函数'''


def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

print(fact(5))


'''尾递归调用，尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式'''


def fact(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

print(fact_iter(5, 1))

print(fact(5))

'''汉诺塔的移动可以用递归函数非常简单地实现。

请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，
然后打印出把所有盘子从A借助B移动到C的方法'''

step = 0


def move(n,a,b,c):
    global step
    if n==1:  #这个地方就是递归函数调用终止的条件
        print(a,'-->',c)
        step=step+1
    else:
        move(n-1,a,c,b)  #把上面n-1个从a-->b
        move(1,a,b,c)    #把最下面一个从a-->c
        move(n-1,b,a,c)  #把上面n-1个从b-->c


def main():
    n=eval(input("please input the numbers of the plates:"))
    move(n,'A','B','C')  #这里的A B C 表示圆柱
    print("the total steps to move the plates from a to c is {}".format(step))


main()
