n = int(input("N: "))
k = 1
f = 1

for i in range(1, n+1):
    f *= i
    k += 1/f

print("!N = ", k)