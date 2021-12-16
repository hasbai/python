def demo(ints: list[int]):
    ints.sort()
    length = len(ints)
    if length == 0:
        return None
    elif length % 2 == 0:
        return (ints[length // 2] + ints[length // 2 - 1]) / 2
    else:
        return ints[(len(ints) - 1) // 2]


ints = eval(input('输入一个整数列表: '))
if demo(ints):
    print('中位数:', demo(ints))
else:
    print('没有中位数')
