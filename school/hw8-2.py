s = input('请输入:')

for i in range(len(s) - 1):
    print(s[:len(s) - i - 1] + ' ' + s[len(s) - i - 1:])

print('-----')

for i in range(len(s) - 1):
    print(s[:i + 1] + ' ' + s[i + 1:])