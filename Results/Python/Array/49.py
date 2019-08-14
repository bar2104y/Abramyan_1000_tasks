from genarr import genRandomArr, genLinearArr
#Самое простое решение O = n^2
n = int(input("N: "))

a = genLinearArr(n, 1)
import random
random.shuffle(a)
print(a)

for i in range(1,n+1):
    f = False
    for j in range(n):
        if a[j] == i:
            f = True
            break
    if not f:
        print(i)
        exit()

print(0)