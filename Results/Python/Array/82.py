#Последовательный сдвиг, используя решение из №80
from genarr import genLinearArr
n = int(input("N: "))
k = int(input("K: "))

a = genLinearArr(n)
print(a)

for j in range(k):
    for i in range(n-1):
        a[i] = a[i+1]

print(a)