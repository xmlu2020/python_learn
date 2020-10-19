def find_second_large_num(num_list):
    tmp_list = sorted(num_list)
    # print(tmp_list)
    print("方法1：second_large_num is:", tmp_list[-2])

    one = num_list[0]
    two = num_list[0]
    # 设置两个标志位一个存储最大数一个存储次大数
    # two 存储次大值，one 存储最大值，遍历一次数组即可，
    # 先判断是否大于 one，若大于将 one 的值给 two，将 num_list[i] 的值给 one，
    # 否则比较是否大于two，若大于直接将 num_list[i] 的值给two，否则pass
    for i in range(1,len(num_list)):
        if num_list[i] > one:
            two = one
            one = num_list[i]
        elif num_list[i] > two:
            two = num_list[i]
    print("方法2：second_large_num_is:", two)


if __name__ == '__main__':
    num_list = [34, 11, 23, 56, 78, 0, 9, 12, 3, 7, 5]
    find_second_large_num(num_list)
    