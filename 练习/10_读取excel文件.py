#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/9/16 15:48
# @Author  : XiaomeiLu
# @FileName: 10_读取excel文件.py
# @Software: PyCharm

import pandas as pd
path = "C:/Users/luxiaomei/Desktop/gongdi0904/events_enter.csv"
path1 = "C:/Users/luxiaomei/Desktop/gongdi0904/zongbiao.xlsx"
df = pd.read_csv(path)
df1 = pd.read_excel(path1)
print(df)
print(df1)