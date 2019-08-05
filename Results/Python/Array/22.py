import random
n = int(input("N: "))
a = []
for i in range(n):
    a.append(int(random.randint(0, 100)))
print(a)

s = 0
k = int(input("K: "))
l = int(input("L: "))

for i in range(n): s+=a[i]

print(s-a[k]-a[l])