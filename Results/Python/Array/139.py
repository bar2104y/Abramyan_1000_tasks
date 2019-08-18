import math
from genarr import genRandomArr
x,y = [], []

n = int(input("N: "))

x,y = genRandomArr(n,-10,10), genRandomArr(n,-10,10)
for i in range(len(x)):
    print(x[i],y[i])

n1 = n
for i in range(len(x)):
    n1 -= 1
    for j in range(n1):
        if x[j+1] < x[j] or (x[j+1] == x[j] and y[j+1] < y[j] ):
            x[j+1], x[j] = x[j], x[j+1]
            y[j+1], y[j] = y[j], y[j+1]

print("-------")
for i in range(len(x)):
    print(x[i],y[i])