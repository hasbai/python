n = int(input())
mod = n % 3
resultLength = int((8*n+4)/6)
intList = input().split()
string = ""
result = []
d = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


for s in intList:
    bString = bin(int(s))
    bLength = len(bString)
    bString = bString[2:bLength]
    bLength = len(bString)
    temp = "00000000" + bString
    bString = temp[bLength:len(temp)]
    string = string + bString

if mod == 1: string = string + "0000"
elif mod == 2: string = string + "00"

for i in range(0,resultLength):
    index = int(string[6 * i:6 * i + 6], 2)
    result.append(d[index])

if mod == 1: result.append("==")
elif mod == 2: result.append("=")

for s in result:
    print(s,end='')
