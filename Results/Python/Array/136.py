import math
from genarr import genRandomArr
x,y = [], []

n = int(input("N: "))

x,y = genRandomArr(n,-10,10), genRandomArr(n,-10,10)

def distanse(x1,y1,x2,y2):
    return(math.sqrt((x2-x1)**2 + (y2-y1)**2))

minm = 100000

for i in range(len(x)):
    print((x[i],y[i]))
    s = 0
    for j in range(len(x)):
        s += distanse(x[i],y[i],x[j],y[j])
    if s < minm:
        ii,jj = i,j
        minm = s

print((x[ii],y[ii]), (x[jj],y[jj]), minm)
