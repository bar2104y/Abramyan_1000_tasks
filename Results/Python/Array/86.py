#взято из №84
from genarr import genLinearArr
n = int(input("N: "))
k = int(input("K: "))

a = genLinearArr(n)
print(a)

for j in range(k):
    tmp = a[0]
    for i in range(n):
        a[i] = a[(i+1)%n]
    a[n-1] = tmp

print(a)