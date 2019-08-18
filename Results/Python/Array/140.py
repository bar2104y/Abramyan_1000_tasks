import math
from genarr import genRandomArr
x,y = [], []

n = int(input("N: "))

x,y = genRandomArr(n,-10,10), genRandomArr(n,-10,10)
for i in range(len(x)):
    print(x[i],y[i])

def compare (x1,y1,x2,y2):
    return( (x1+y1 < x2+y2) or ( (x1+y1 == x2+y2) and x1<x2) )

n1 = n
for i in range(len(x)):
    n1 -= 1
    for j in range(n1):
        if compare(x[j],y[j], x[j+1], y[j+1]):
            x[j+1], x[j] = x[j], x[j+1]
            y[j+1], y[j] = y[j], y[j+1]

print("-------")
for i in range(len(x)):
    print(x[i],y[i])