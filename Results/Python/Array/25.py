n = int(input())
a=[]
A = 1
D = 2
for i in range(n):
    a.append(A+D**i)

A = a[0] - 1
D = a[1] - A

for i in range(n):
    if A+D**i != a[i]:
        exit("0")

print("Yes")