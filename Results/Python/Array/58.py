'''
Из-за нумерации с нуля приходится использовать костыли, я правда не хотел этого делать
'''

from genarr import genRandomArr
n = int(input("N: "))

a = genRandomArr(n,0,5)
print(a)

b = []
sum = 0

for i in range(1,n):
    sum += a[i]
    b.append(sum)

print(b)