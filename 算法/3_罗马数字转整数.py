#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/9/8 20:42
# @Author  : XiaomeiLu
# @FileName: 3_罗马数字转整数.py
# @Software: PyCharm


# def romanToInt(s):
#     """
#     :type s: str
#     :rtype: int
#     """
#     result = 0
#     temp_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
#     for i in range(len(s)-1):
#         if temp_dict[s[i]] < temp_dict[s[i+1]]:
#             result -= temp_dict[s[i]]
#         else:
#             result += temp_dict[s[i]]
#     result += temp_dict[s[-1]]
#     return result

def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    result = 0
    temp_list = []
    for i in s:
        if i == 'I':
            temp_list.append(1)
        elif i == 'V':
            temp_list.append(5)
        elif i == 'X':
            temp_list.append(10)
        elif i == 'L':
            temp_list.append(50)
        elif i == 'C':
            temp_list.append(100)
        elif i == 'D':
            temp_list.append(500)
        elif i == 'M':
            temp_list.append(1000)
    print(temp_list)
    for j in range(len(temp_list)):
        if j == len(temp_list) - 1:
            result += temp_list[j]
        else:
            if temp_list[j] < temp_list[j + 1]:
                result -= temp_list[j]
            else:
                result += temp_list[j]
    return result


if __name__ == '__main__':
    s = "XXVII"
    print(romanToInt(s))


