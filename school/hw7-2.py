print('1 = (0 + 1) **2')
for n in range(10, 100001):
    s = str(n)
    for i in range(1, len(s)):
        a = int(s[:i])
        b = int(s[i:])
        if(n == (a + b)**2):
            print(f'{n} = ({a} + {b}) **2')
