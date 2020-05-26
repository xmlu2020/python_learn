# -*- coding: utf-8 -*-
# @Time    : 2020/7/14 00:13
# @Author  : XiaomeiLu
# @FileName: 3_2高级特性_列表生成式.py
# @Software: PyCharm
import os

print(list(range(1, 11)))

L = []
for x in range(1,11):
    L.append(x * x)
print(L)

print([x * x for x in range(1,11)])

print([x * x for x in range(1, 11) if x % 2 == 0])

print([m + n for m in 'ABC' for n in 'XYZ'])


'列出当前目录下的所有文件和目录名，可以通过一行代码实现'
print([d for d in os.listdir('.')])

d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k, v in d.items():
    print(k, '=', v)
d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + '=' + v for k,v in d.items()])

L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])


print([x if x % 2 == 0 else -x for x in range(1,11)])

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s,str)]

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')