import random

tup = tuple([random.randint(1, 99) for i in range(10)])
result = [i for i in tup if i > 50]

print(f'随机生成的元组：{tup}')
print(f'该元组中所有大于50的元素：{result}')
