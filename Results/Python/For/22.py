n = int(input("N: "))
x = int(input("X: "))
k = 1
f = 1

for i in range(1, n+1):
    f *= i
    k += x ** i/f

print("!N = ", k)