#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/6 21:44
# @Author  : XiaomeiLu
# @FileName: 2_函数.py
# @Software: PyCharm

'调用函数'
'利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：'
n1 = 255
n2 = 1000

print(hex(n1))
print(hex(n2))


'定义函数'
'''
定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程 ax^2+bx+c=0
计算平方根可以调用math.sqrt()函数：'''

import math


def PFG(a,b,c):
    #math.sqrt() 计算平方根
    x1 = (-b+(math.sqrt((b**2)-4*a*c)))/(2*a)
    x2 = (-b-(math.sqrt((b**2)-4*a*c)))/(2*a)
    return x1,x2
print("请输入a，按回车结束输入")
x = input()
print("请输入b，按回车结束输入")
y = input()
print("请输入c，按回车结束输入")
z = input()
p = PFG(int(x),int(y),int(z))
print('第一个根是',p[0])
print('第二个根是',p[1])


