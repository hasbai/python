import math
for i in range(1,1000):
    if i == math.pow((i//100),3)+math.pow(((i%100)//10),3)+math.pow(i%10,3) == i:
        print(i)
