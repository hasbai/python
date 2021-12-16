def mysum(ints: list[int]) -> int:
    if len(ints) == 0:
        return 0
    return ints[0] + mysum(ints[1:])


ints = eval(input('输入一个整数列表：'))
print('数值之和：', mysum(ints))
