import random
n = int(input("N: "))
a = []

m = 200
i = 0

################
for i in range(n):
    a.append(random.randint(0,100))
print(a)
################

while i < n:
    if a[i] < m: m = a[i]
    i += 2 

print(m)