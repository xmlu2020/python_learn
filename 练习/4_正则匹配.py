#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/9/15 20:20
# @Author  : XiaomeiLu
# @FileName: 4_正则匹配.py
# @Software: PyCharm

import re
str = '<div class="nam">中国</div>'
res = re.findall(r'<div class=".*">(.*?)</div>', str)
print(res)
