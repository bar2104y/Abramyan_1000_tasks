from genarr import genLinearArr
n = int(input("N: "))
k = int(input("K: "))

a = genLinearArr(n)
print(a)

#a.insert(k+1, 0)
tmp1 = a[k+1]
a[k+1] = 0
for i in range(k+1,n-1):
    tmp = a[i+1]
    a[i+1] = tmp1
    tmp1 = tmp

a.append(tmp1)


print(a)