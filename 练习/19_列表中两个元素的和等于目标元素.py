#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/10/3 13:53
# @Author  : XiaomeiLu
# @FileName: 19_列表中两个元素的和等于目标元素.py
# @Software: PyCharm


class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            num = target - nums[i]
            if num in nums[i+1:]:
                return [i, nums.index(num)]


solution = Solution()
list = [2, 11, 6, 7]
target = 9
nums = solution.twoSum(list, target)
print(nums)