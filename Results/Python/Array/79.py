from genarr import genLinearArr
n = int(input("N: "))

a = genLinearArr(n)
print(a)

tmp = a[0]
a[0] = 0

for i in range(n):
    tmp1 = a[i]
    a[i] = tmp
    tmp = tmp1  
    
print(a)