#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/14 16:15
# @Author  : XiaomeiLu
# @FileName: 4_1高阶函数_map_reduce.py
# @Software: PyCharm

from functools import reduce

'''变量可以指向函数'''


def add (x,y,f):
    return f(x) + f(y)


print(add(-5,6,abs))


'''
map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。

举例说明，比如我们有一个函数f(x)=x2，要把这个函数作用在一个list [1, 2, 3, 4, 5, 6, 7, 8, 9]上，就可以用map()实现如下

'''


def f(x):
    return x * x


r = map(f, [1,2,3,4,5,6,7,8,9])
print(list(r))

'''
map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，
Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list
把这个list所有数字转为字符串
'''
print(list(map(str, [1,2,3,4,5,6,7,8,9])))


'''
reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是
'''

# reduce(f,[x1,x2,x3,x4]) = f(f(f(x1,x2),x3),x4)

<<<<<<< HEAD
'''对一个序列求和'''

=======
>>>>>>> 9647d989de56718953060a3a5cfb695235e2e969

def add(x,y):
    return x + y

<<<<<<< HEAD
=======

print(reduce(add, [1, 3, 5, 7, 9]))






>>>>>>> 9647d989de56718953060a3a5cfb695235e2e969

print(reduce(add, [1, 3, 5, 7, 9]))

'''把序列[1,3,5,7,9]变换成13579'''


def fn(x,y):
    return x * 10 + y


print(reduce(fn, [1, 3, 5, 7, 9]))

'''把str转换成int函数'''


def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


print(reduce(fn, map(char2num, '13579')))


DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2int(s):
    def fn(x,y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    print(reduce(fn, map(char2num, s)))
    return reduce(fn,map(char2num,s))


def char2num(s):
    return DIGITS[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


"""练习

利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，
其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']："""


def normalize(name):
    name = name[0].upper() + name[1:].lower()
    return name


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


def prod(L):
    return reduce(lambda x, y: x * y, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')
