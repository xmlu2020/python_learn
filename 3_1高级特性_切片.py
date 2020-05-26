# -*- coding: utf-8 -*-
# @Time    : 2020/7/13 17:30
# @Author  : XiaomeiLu
# @FileName: 3_1高级特性_切片.py
# @Software: PyCharm

'切片'
'取前三个元素'
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# print(L[0:3])
print(L[:3])
print(L[-2:])
print(L[-2:-1])

L = list(range(100))
print(L)
'前10'
print(L[:10])
'后10'
print(L[-10:])
'11到20'
print(L[10:20])
'前10个每两个取1个'
print(L[:10:2])
'所有数，每5个取一个'
print(L[::5])
'复制一个list'
print(L[:])

print('ASDFGHJKL'[:3])

'利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：'


def trim(s):
    if len(s) == 0:
        return s
    elif s[0] == " ":
        return (trim(s[1:]))
    elif s[-1] == " ":
        return (trim(s[:-1]))
    return s


# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')


