#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/10/3 21:41
# @Author  : XiaomeiLu
# @FileName: 22_统计文本中单词频次最高的10个单词.py
# @Software: PyCharm
import re
import os
from collections import Counter


def test(filepath):
    """
           :param filepath: 文件路径
           :return:
           """
    with open(filepath, 'r') as file:
        for lines in file:
            lines = re.sub('\W+', ' ', lines)
        print(lines)
        dict_word = {}
        for i in range(0, len(lines.split(' '))):
            word = lines.split(' ')[i]
            if word not in dict_word:
                dict_word[word] = 1
            else:
                dict_word[word] += 1
        word_sorted = sorted(dict_word.items(), key=lambda x: x[1], reverse=True)
        for i in range(0, 10):
            print(word_sorted[i])


# def test2(filepath):
#     with open(filepath) as f:
#         return list(map(lambda c:c[10],Counter(re.sub("\w+"," ",f.read()).split()).most_common(10)))


if __name__ == '__main__':
    filepath = os.path.join(os.path.abspath(os.path.join(os.getcwd(), '..')), 'f1.log')
    print(test(filepath))