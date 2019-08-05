import random

n = int(input("N: "))
a = [random.randint(0, 100) for i in range(n)]

print(a)

s = 0
k = int(input("K: "))
l = int(input("L: "))
cnt = l-k+1

while k <= l:
    s += a[k]
    k += 1

print(s/cnt)