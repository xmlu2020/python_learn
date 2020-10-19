
"""
新列表中的元素为原始列表的偶数切片
"""
list_data = [1, 2, 5, 8, 10, 3, 18, 6, 20]
res = [x for x in list_data[::2] if x % 2 == 0]
print(res)

"""
一行代码生成[1，4，9，16，25，36，49，64，81，100]
"""

list = [x * x for x in range(1, 11)]
print(list)