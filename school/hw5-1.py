dic = {
    1: 'One',
    2: 'Two',
    3: 'Three',
    4: 'Four',
    5: 'Five'
}

key = int(input('Please input a key:'))
value = dic.get(key)

output = value if value else '您输入的键有误！'
print(output)
