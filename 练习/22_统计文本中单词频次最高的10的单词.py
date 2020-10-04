#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/10/3 21:41
# @Author  : XiaomeiLu
# @FileName: 22_统计文本中单词频次最高的10的单词.py
# @Software: PyCharm
import re


def test(filepath):
    distone = {}
    with open(filepath) as f:
        for line in f:
            line = re.sub("\w+", " ", line)