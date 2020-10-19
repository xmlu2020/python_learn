
def fun1(l):
    if isinstance(l, str):  #判断一个对象是不是已知类型
        l = [int(i) for i in l]   # 字符串转成list
        l.sort(reverse=True)   # 从大到小排序
        for i in range(len(l)):
            if l[i] % 2 > 0:
                l.insert(0,l.pop(i))
        print(''.join(str(e) for e in l))  # 列表转成字符串


if __name__ == '__main__':
    l = "1982376455"
    fun1(l)