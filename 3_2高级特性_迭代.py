# -*- coding: utf-8 -*-
# @Time    : 2020/7/13 18:46
# @Author  : XiaomeiLu
# @FileName: 3_2高级特性_迭代.py
# @Software: PyCharm

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)

for value in d.values():
    print(value)

for k,v in d.items():
    print(k, v)

for ch in 'ABC':
    print(ch)

# from collections import Iterable
# isinstance('abc',Iterable)
#
# isinstance([1,2,3],Iterable)
#
# isinstance(123,Iterable)

'Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身'

for i,value in enumerate(['A','B','C']):
    print(i,value)

for x,y in [(1,1),(2,4),(3,9)]:
    print(x,y)


def findMinAndMax(L):
    if L!=[]:
        (max,min) = (L[0],L[0])
        for x in L:
            if x > max:
                max = x
            if x < min:
                min = x
        return(max,min)
    else:
        return(None,None)


if findMinAndMax([]) != (None,None):
    print('测试失败！')
elif findMinAndMax([7]) != (7,7):
    print('测试失败！')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7,1]) != (7, 1):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (9, 1):
    print('测试失败!')
else:
    print('测试成功！')

