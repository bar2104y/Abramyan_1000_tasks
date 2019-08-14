from genarr import genLinearArr
n = int(input("N: "))
k = int(input("K: "))
l = int(input("L: "))

a = genLinearArr(n)
print(a)
#0123456789
h = (l-k-1)//2
j = 0

for i in range(k+1, k+h+1):
    a[i], a[l-1-j] = a[l-1-j], a[i]
    j += 1
print(a)
    