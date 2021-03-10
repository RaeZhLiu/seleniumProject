def cycle_line(str):
    length = len(str) - 1

    for i in range(length):
        if i < length and str[i] != str[length]:
            print(str, "非回文数")
            return
        elif i >= length:
            print(str, "是回文数")
            break
        length -= 1


if __name__ == '__main__':
    str = input("请输入要验证的字符串：")
    cycle_line(str)



