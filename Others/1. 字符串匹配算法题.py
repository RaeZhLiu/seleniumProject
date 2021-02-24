from icecream import ic
if __name__ == '__main__':

    a = 'abcdefj'
    b = 'abc'

    if b in a:
        # 1：使用字符串切片，实现字符串翻转
        a = a[::-1]
        ic(a)
        # 2：使用reversed方法，缺点是速度慢
        a = ''.join(reversed(a))
        # a = ''.join(['a', 'b', 'c'])
        print(a, "+", type(a))
    #     for i in range(len(a), 0):
    #         tmp.append(a[i])
    #     a = str(tmp)
    #     print(a)


