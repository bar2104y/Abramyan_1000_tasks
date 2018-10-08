print("!N")
n = int(input("N: "))
k = 0
f = 1

for i in range(1, n+1):
    f *= i
    k += f

print("!N = ", k)