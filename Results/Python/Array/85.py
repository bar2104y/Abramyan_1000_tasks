#Последовательный сдвиг, используя решение из №83
from genarr import genLinearArr
n = int(input("N: "))
k = int(input("K: "))

a = genLinearArr(n)
print(a)

for j in range(k):
    tmp = a[0]

    for i in range(n):
        tmp1 = a[(i+1)%n]
        a[(i+1)%n] = tmp
        tmp = tmp1  
        
print(a)