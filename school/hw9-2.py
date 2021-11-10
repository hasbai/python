import re

s = input('请输入一段英文：')

s = re.sub(r'\bi\b', 'I', s)
s = re.sub(r'(\BI)|(I\B)', 'i', s)

print(s)
