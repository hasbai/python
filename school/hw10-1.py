import re

s = input('请输入一段英文：')

words = re.findall(r'\b\S+?\b', s)
words = set(words)
words = list(words)

i = 1
while words:
    result = []
    for word in words:
        if len(word) == i:
            result.append(word)
            words.remove(word)
    if result:
        print(f'长度为{i}:', ', '.join(result))
    i += 1
