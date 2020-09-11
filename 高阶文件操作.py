#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/31 11:51
# @Author  : XiaomeiLu
# @FileName: 高阶文件操作.py
# @Software: PyCharm

import shutil
'''将文件内容拷贝到另一个文件中'''
shutil.copyfileobj(open('old.xml', 'r'), open('new.xml', 'w'))

'''拷贝文件,目标文件无需存在'''
shutil.copyfile('f1.log', 'f2.log')

'''仅拷贝权限。内容、组、用户均不变,目标文件必须存在'''
shutil.copymode('f1.log', 'f2.log')

'''仅拷贝状态的信息，包括：mode bits, atime, mtime, flags,目标文件必须存在'''
shutil.copystat('f1.log', 'f2.log')

'''拷贝文件和权限'''
shutil.copy('f1.log', 'f2.log')

'''拷贝文件和状态信息'''
shutil.copy2('f1.log', 'f2.log')

'''递归拷贝文件,目标目录不能存在，注意对folder2目录父级目录要有可写权限，ignore的意思是排除'''
shutil.copytree('folder1', 'folder2', ignore=shutil.ignore_patterns('*.pyc', 'tmp*'))

'''递归的去删除文件'''
shutil.rmtree('folder1')

'''递归的去移动文件，类似mv，其实就是重命名'''
shutil.move('folder1', 'folder3')

'''创建压缩包并返回文件路径，例如：zip、tar'''

'''将 /data 下的文件打包放置当前程序目录'''

ret = shutil.make_archive("data_bak", 'gztar', root_dir='/data')

'''将 /data下的文件打包放置 /tmp/目录'''

ret1 = shutil.make_archive("/tmp/data_bak", 'gztar', root_dir='/data')


import os
import shutil


vt_image_path = "./20200615"
pid_image_path = "/ssd/yan/purity_merge/direct/K11_gz_mall_20200615/fid_images"

output_path = "./4label"
os.makedirs(output_path, exist_ok=True)

pid_ptks = {}
for l in open("./ptk_pid_daily_allfaces.csv", "r").readlines():
    ptk, pid = l.strip().split(",")
    pid_ptks.setdefault(pid, [])
    pid_ptks[pid].append(ptk)


for vt_image in os.listdir(vt_image_path):
    pid = vt_image[:-4]
    if pid not in pid_ptks.keys():
        continue
    print("processing .... ", pid, vt_image)
    pid_path = os.path.join(output_path, pid)
    os.makedirs(pid_path, exist_ok=True)
    shutil.copy(os.path.join(vt_image_path, vt_image), os.path.join(pid_path, vt_image))
    for ptk in pid_ptks[pid][:3]:
        print("\tcopying image ", ptk)
        try:
            shutil.copy(os.path.join(pid_image_path, 'face', ptk+'.jpg'), os.path.join(pid_path, ptk+'face.jpg'))
            shutil.copy(os.path.join(pid_image_path, 'body', ptk+'.jpg'), os.path.join(pid_path, ptk+'body.jpg'))
        except Exception as e:
            print(e)

