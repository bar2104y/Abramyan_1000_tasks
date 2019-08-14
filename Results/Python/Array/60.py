from genarr import genRandomArr
n = int(input("N: "))

a = genRandomArr(n,0,5)
a[0] = 0
print(a)

b = []
sum = 0
for i in range(n):
    sum += a[i]

for i in range(1,n):
    b.append(sum)
    sum -= a[i]    

print(b)