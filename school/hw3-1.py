import math

if __name__ == '__main__':
    li = input('输入一个列表')
    li = eval(li)
    odd = [li[i * 2] for i in range(math.ceil(len(li) / 2))]
    even = [li[i * 2 + 1] for i in range(len(li) // 2)]
    print(f'奇数项子列表：{odd}')
    print(f'偶数项子列表：{even}')
