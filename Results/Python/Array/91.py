from genarr import genLinearArr
n = int(input("N: "))
k = int(input("K: "))
l = int(input("L: "))

a = genLinearArr(n)
print(a)

d = l-k+1

for i in range(k,l+1):
    a.pop(k)
    
print(a)
