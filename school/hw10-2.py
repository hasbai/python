import re

s = input('请输入html文本：')

s = re.sub(r'<.+?>', '', s)

print(s)
