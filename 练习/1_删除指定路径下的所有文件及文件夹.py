#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/9/15 17:03
# @Author  : XiaomeiLu
# @FileName: 1_删除指定路径下的所有文件及文件夹.py
# @Software: PyCharm


import os


def delete(filepath):
    files = os.listdir(filepath)
    for file in files:
        f = os.path.join(filepath, file)
        print(f)
        if os.path.isdir(f):  # 如果f是文件夹
            if not os.listdir(f):  # 如果f路径下为空
                # os.listdir()方法用于返回指定的文件夹包含的文件或文件夹的名字的列表
                os.rmdir(f)
            else:  # 如果f不为空，则递归
                delete(f)
                if not os.listdir(f):
                    os.rmdir(f)
        elif os.path.isfile(f):
            os.remove(f)

    print("删除完毕")


if __name__ == '__main__':
    filepath = "C:/Users/luxiaomei/Desktop/new"
    delete(filepath)

