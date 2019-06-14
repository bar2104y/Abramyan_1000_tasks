import math

def TriangleP(a,h):
    b = math.sqrt( (a/2)**2 + h*h )
    return(b+b+a)

arr = [[8, 3], [2,1], [5,2]]
for i in arr:
    print(TriangleP(i[0],i[1]))