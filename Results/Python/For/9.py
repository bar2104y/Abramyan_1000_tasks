print("A < B")
a = int(input("A: "))
b = int(input("B: "))
k = 0

for i in range(a, b+1):
    k += i * i

print("R = ", k)