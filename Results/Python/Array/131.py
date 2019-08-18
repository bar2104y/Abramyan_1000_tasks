import math
x = []
y = []

n = int(input("N: "))
for i in range(n):
    x.append(int(input("X: ")))
    y.append(int(input("Y: ")))

bx,by = int(input("Bx: ")), int(input("By: "))

def distanse(x1,y1,x2,y2):
    return(math.sqrt((x2-x1)**2 + (y2-y1)**2))

mind = 10000

for i in range(len(x)):
    d = distanse(x[i],y[i], bx,by)
    if d < mind:
        mind = d
        j = i

print((x[j],y[j]))