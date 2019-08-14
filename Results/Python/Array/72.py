from genarr import genLinearArr
n = int(input("N: "))
k = int(input("K: "))
l = int(input("L: "))

a = genLinearArr(n)
print(a)

h = (l-k)//2+1
j = 0

for i in range(k, k+h):
    a[i], a[l-j] = a[l-j], a[i]
    j += 1
print(a)
    