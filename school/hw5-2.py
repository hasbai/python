import random

li = [random.randint(1, 10) for i in range(20)]

dic = {}
for i in range(10):
    dic[i+1] = 0

for num in li:
    dic[num] += 1

print('随机生成的列表:', li)
print('value: count')
for i in dic:
    print(f'{i}: {dic[i]}')