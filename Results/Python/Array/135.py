import math
from genarr import genRandomArr
x1,y1 = [],[]
x2,y2 = [],[]
n1 = int(input("N1: "))
n2 = int(input("N2: "))

x1,y1 = genRandomArr(n1,-10,10), genRandomArr(n1,-10,10)
x2,y2 = genRandomArr(n2,-10,10), genRandomArr(n2,-10,10)

print(x1)
print(y1)
print()
print(x2)
print(y2)
print()

def distanse(x1,y1,x2,y2):
    return(math.sqrt((x2-x1)**2 + (y2-y1)**2))

mind = 10000

for i in range(len(x1)):
    for j in range(len(x2)):
        d = distanse(x1[i],y1[i],x2[j],y2[j])
        if d < mind:
            ii,jj = i,j
            maxd = d

print((x1[ii],y1[ii]), (x2[jj],y2[jj]), distanse(x1[ii],y1[ii], x2[jj],y2[jj]))
