#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/14 10:29
# @Author  : XiaomeiLu
# @FileName: 3_4高级特性_生成器.py
# @Software: PyCharm

L = [x * x for x in range(10)]
print("**********")
print(L)

g = (x * x for x in range(10))
# print(next(g))
for n in g:
    print("**********")
    print(n)

'斐波拉契数列用列表生成式写不出来，但是，用函数把它打印出来却很容易'


def fib(max):
    n, a, b = 0, 0,1
    while n <max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


# fib(6)
for n in fib(6):
    print("**********")
    print(n)

'''
要把fib函数变成generator，只需要把print(b)改为yield b就可以了
这就是定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
'''


def fib_generator(max):
    n ,a ,b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


g = fib_generator(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:',e.value)
        break


def odd():
    print("step 1")
    yield (1)
    print("step 2")
    yield (3)
    print("step 3")
    yield (5)

o = odd()

print(next(o))

'''杨辉三角定义如下：

          1
         / \
        1   1
       / \ / \
      1   2   1
     / \ / \ / \
    1   3   3   1
   / \ / \ / \ / \
  1   4   6   4   1
 / \ / \ / \ / \ / \
1   5   10  10  5   1
把每一行看做一个list，试写一个generator，不断输出下一行的list：'''


def triangles():
    L = [1]
    while True:
        yield L
        L.append(0) # 想一想还是觉得很巧妙呀，在最后一个加上0，不管是第一个数或是最后一个数都是1+0
        L = [L[i - 1] + L[i] for i in range(len(L))]

n = 0
for t in triangles():
    print(t)
    if n == 10:
        break
    else:
        n += 1




# 杨辉三角
# def triangles():
#     n = 1
#     l_list = [1]
#     while True:
#         yield l_list
#         n += 1
#         i = 0
#         l_temp = l_list
#         l_list = []
#         for i in range(0, n):
#             if i == 0 or i == n - 1:
#                 l_list.append(1)
#             else:
#                 l_list.append(l_temp[i - 1] + l_temp[i])



