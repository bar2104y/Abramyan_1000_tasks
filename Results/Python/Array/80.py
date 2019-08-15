from genarr import genLinearArr
n = int(input("N: "))

a = genLinearArr(n)
print(a)

tmp = a[0]

for i in range(n-1):
    a[i] = a[i+1]

a[n-1] = 0
print(a)