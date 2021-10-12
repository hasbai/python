if __name__ == '__main__':
    li = input('输入一个列表')
    li = eval(li)
    result = []
    for i in li:
        result.extend([i, i])
    print(f'结果列表：{result}')
