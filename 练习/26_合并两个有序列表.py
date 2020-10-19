"""
使用python自带的extend方法
"""
L1=[23,45,67,77,78,80,90]
L2=[4,11,26,33,42,61,80]
L1.extend(L2)
L1.sort()
print(L1)


"""
使用循环比较的方法
"""


def loop_merge_sort(l1,l2):
    tmp=[]
    while len(l1)>0 and len(l2)>0:
        if l1[0]<l2[0]:   #每次循环比较第一个元素
            tmp.append(l1[0])
            del l1[0]
        else:
            tmp.append(l2[0])
            del l2[0]
    while len(l1)>0:
        tmp.append(l1[0])
        del l1[0]
    while len(l2)>0:
        tmp.append(l2[0])
        del l2[0]
    return tmp


if __name__ == '__main__':
    L1 = [23, 45, 67, 77, 78, 80, 90]
    L2 = [4, 11, 26, 33, 42, 61, 80]
    new_list = loop_merge_sort(L1, L2)
    print(new_list)