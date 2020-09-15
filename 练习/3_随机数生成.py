#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/9/15 20:08
# @Author  : XiaomeiLu
# @FileName: 3_随机数生成.py
# @Software: PyCharm
import random

import numpy as np

result = random.randint(10, 20)
res = np.random.randn(5)
ret = random.random()
print("随机整数", result)
print("随机小数", res)
print("0-1随机小数", ret)