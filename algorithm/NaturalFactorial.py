import math
def factorial(n):
    if n == 1 : return n
    return n*factorial(n-1)

input = input()
temp = input.split()
n = int(temp[0])
p = int(temp[1])
f = factorial(n + p)
print(int((f+math.e)) % n)
