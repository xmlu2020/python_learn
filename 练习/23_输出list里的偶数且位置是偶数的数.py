
def num_list(num):
    return [i for i in num if i % 2 == 0 and num.index(i) % 2 == 0]


if __name__ == '__main__':
    num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = num_list(num)
    print(result)
