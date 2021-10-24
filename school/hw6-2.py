import random

li = [random.randint(1, 20) for i in range(10)]
print('随机生成的列表：', li)

li.sort()

target_index = -1
for i in range(len(li)):
    if li[i] > 10:
        target_index = i
        break
li = li[:target_index]

print('删除元素后的列表：', li)