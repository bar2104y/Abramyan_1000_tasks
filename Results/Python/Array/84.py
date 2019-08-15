from genarr import genLinearArr
n = int(input("N: "))

a = genLinearArr(n)
print(a)

tmp = a[0]

for i in range(n):
    a[i] = a[(i+1)%n]

a[n-1] = tmp
print(a)