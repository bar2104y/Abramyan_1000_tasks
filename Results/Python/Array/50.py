from genarr import genRandomArr, genLinearArr
#Самое простое решение O = n^2
n = int(input("N: "))

a = genLinearArr(n, 1)
import random
random.shuffle(a)
print(a)
cnt = 0

for i in range(n):
    for j in range(i+1,n):
        if a[i] > a[j]:
            cnt += 1


print(cnt)