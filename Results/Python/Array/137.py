import math
from genarr import genRandomArr
x,y = [], []

n = int(input("N: "))

x,y = genRandomArr(n,-10,10), genRandomArr(n,-10,10)

def distanse(x1,y1,x2,y2):
    return(math.sqrt((x2-x1)**2 + (y2-y1)**2))

mp = 0

for i in range(len(x)):
    print(x[i],y[i])
    for j in range(i+1, len(x)):
        for k in range(j+1, len(x)):
            a = distanse(x[i], y[i], x[j], y[j])
            b = distanse(x[k], y[k], x[j], y[j])
            c = distanse(x[k], y[k], x[i], y[i])
            if a+b+c >mp:
                mp = a+b+c
                i1,i2,i3 = i,j,k

print((x[i1],y[i1]), (x[i2],y[i2]), (x[i3],y[i3]),mp)