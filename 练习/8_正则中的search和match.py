#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/9/16 14:41
# @Author  : XiaomeiLu
# @FileName: 8_正则中的search和match.py
# @Software: PyCharm

import re
s = "小明年龄18岁 工资10000"
res = re.search(r"\d+", s).group()  # search 匹配到第一个匹配到的数据
print("search结果", res)

res = re.findall(r"\d+", s)
print("findall结果", res)   # findall 满足正则，都匹配，不用加group

res = re.match("小明", s).group()  # 匹配以小明开头的字符串，并匹配出小明
print("match结果", res)

res = re.match(r"\d+", s)  # 不加group是不对的
print("试错，不加group为none，匹配不到", res)

res = re.match("工资", s).group()  # 工资不是字符串开头，匹配不到，报错
print("match结果", res)
