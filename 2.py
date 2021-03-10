"""
完数：6 = 1+2+3
"""


def ws(num):
    sum = 0
    num_1 = num / 2 + 1
    for i in range(1, num_1):
        if num % i == 0:
            print(i)
            sum += i

    return sum == num


if __name__ == '__main__':

    num = int(input("输入数值："))
    if ws(num):
        print('%d 是完数' % num)
