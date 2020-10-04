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

"""
匹配中文字符的正则表达式： [\u4e00-\u9fa5]
匹配双字节字符(包括汉字在内)：[^\x00-\xff]
英文字母:[a-zA-Z]
数字:[0-9]

"""

title = '你好，hello，世界'
pattern = re.compile(r'[\u4e00-\u9fa5]+')  # 匹配中文
result = pattern.findall(title)

print(result)

s = '"http://eventsapi.aibee.cn/ssd/tliu/ZHDC/foshan/hyc/post/20200625_comp/ch10008_20200625151256-00154272' \
    '-ch10008_20200625151256-00154272.comp.html",' \
    '"id=zhdc-foshan-hyc-L508-N", "ch = ch10008_20200625150500-00154272_ch10008_20200625151256-00154272",' \
    '"time=15:16:49","ch10008_20200625150500-00154272"' \
    '"http://eventsapi.aibee.cn/ssd/tliu/ZHDC/foshan/hyc/post/20200625_comp/ch10008_20200625151256-00154272' \
    '-ch10008_20200625151256-00154272.comp.html" '

res = re.findall(r"http://.*?\.html", s)[0]  # 提取第一个URL
print(res)
res = re.search(r"http://.*?\.html", s)  # search需要加group()
print(res.group())

tels = ["13100001234", "18912344321", "10086", "18800007777"]
for tel in tels:
    ret = re.match('1\d{9}[0-3,5-6,8-9] ', tel)   # 匹配手机号
    if ret:
        print("想要的结果", ret.group())
    else:
        print("%s 不是想要的手机号" % tel)


email_list = ["xiaoWang@163.com", "xiaoWang@163.comheihie", ".com.xiaowang@qq.com"]
for email in email_list:
    ret = re.match("[\w]{4,20}@163\.com$", email)
    if ret:
        print("%s 是符合规定的邮件地址，匹配后的结果是：%s" % (email, ret.group()))
    else:
        print("%s 不符合要求" % email)