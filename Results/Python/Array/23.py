import random
n = int(input("N: "))
a = []
for i in range(n):
    a.append(int(random.randint(0, 10)))
print(a)

s = cnt = 0
k = int(input("K: "))
l = int(input("L: "))

for i in range(n):
    if i not in range(k,l+1):
        s+=a[i]
        cnt += 1
        
print(s/cnt)
