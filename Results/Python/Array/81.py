#Последовательный сдвиг, используя решение из №79
from genarr import genLinearArr
n = int(input("N: "))
k = int(input("K: "))

a = genLinearArr(n)
print(a)

tmp = a[0]
a[0] = 0

for j in range(k):
	for i in range(n):
		tmp1 = a[i]
		a[i] = tmp
		tmp = tmp1 

for i in range(k):
    	a[i] = 0
    
print(a)