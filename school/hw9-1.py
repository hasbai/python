li = input('请输入两个单词，以空格分隔：').split()
a = li[0]
b = li[1]
aa = a
bb = b

result = len(a) == len(b)

while(len(a) > 0):
    char = a[0]
    result = result and a.count(char) == b.count(char)
    a = a.replace(char, '')
    b = b.replace(char, '')

result = '不' if not result else ''
print(f'单词{aa}与单词{bb}{result}是相似词！')
