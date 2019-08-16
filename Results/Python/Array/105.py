from genarr import genLinearArr
n = int(input("N: "))
k = int(input("K: "))
m = int(input("M: "))

a = genLinearArr(n)
print(a)

for i in range(m):
    a.insert(k+1,0)

print(a)