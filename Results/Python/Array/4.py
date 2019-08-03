a = []
n = int(input("N: "))
A = int(input("A: "))
D = int(input("D: "))

for i in range(n):
    a.append(A+D**i)

print(a)