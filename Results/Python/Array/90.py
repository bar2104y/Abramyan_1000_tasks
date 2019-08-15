from genarr import genLinearArr
n = int(input("N: "))
k = int(input("K: "))

a = genLinearArr(n)
print(a)

for i in range(k,n):
    a.pop(k)

print(a)
