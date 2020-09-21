#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/9/18 20:17
# @Author  : XiaomeiLu
# @FileName: 15_字典和json字符串转化.py
# @Software: PyCharm
import json

dic = {"name": "zs"}
res = json.dumps(dic)
print(res, type(res))
ret = json.loads(res)
print(ret, type(ret))