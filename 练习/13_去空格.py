#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/9/18 20:08
# @Author  : XiaomeiLu
# @FileName: 13_去空格.py
# @Software: PyCharm
import re

str = "hello world ha ha"
res = str.replace(" ", "")
print(res)

list = str.split(" ")
res = "".join(list)
print(res)

s = "info:xiaozhang 33 shandong"
ret = re.split(r":| ", s)
print(ret)
