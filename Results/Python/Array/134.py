import math
from genarr import genRandomArr
x,y = [], []

n = int(input("N: "))
# for i in range(n):
#     x.append(int(input("X: ")))
#     y.append(int(input("Y: ")))

x,y = genRandomArr(n,-10,10), genRandomArr(n,-10,10)

def distanse(x1,y1,x2,y2):
    return(math.sqrt((x2-x1)**2 + (y2-y1)**2))

maxd = 0

for i in range(len(x)):
    print((x[i],y[i]))
    for j in range(i+1,len(x)):
        d = distanse(x[i],y[i],x[j],y[j])
        if d > maxd:
            ii,jj = i,j
            maxd = d

print((x[ii],y[ii]), (x[jj],y[jj]), distanse(x[ii],y[ii], x[jj],y[jj]))
