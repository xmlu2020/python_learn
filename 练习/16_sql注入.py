#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/9/18 20:32
# @Author  : XiaomeiLu
# @FileName: 16_sql注入.py
# @Software: PyCharm

# SQL注入
# 例如一条SQL语句是：
import pymysql

input_name = "zs"
sql = 'select * frm demo where name="%s"' % input_name
print("正常SQL语句", sql)

input_name = "zs;drop database demo"
sql = 'select * frm demo where name="%s"' % input_name
print("SQL注入语句", sql)

# 通过参数化方式解决SQL注入
# conn = pymysql.connect(host="localhost",db="学生信息",user="root",password="ydp19941121",charset="utf8")
# cs1 = conn.cursor()
# params = ['zs']
# count = cs1.execute('select * frm demo where name=%s', params)