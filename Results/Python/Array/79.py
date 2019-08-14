from genarr import genLinearArr
n = int(input("N: "))

a = genLinearArr(n)
print(a)

tmp = a[0]

for i in range(n):
    tmp1 = a[(i+1)%n]
    a[(i+1)%n] = tmp
    tmp = tmp1  
    
print(a)