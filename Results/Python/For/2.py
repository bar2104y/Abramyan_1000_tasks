print("A < B")
a = int(input("A: "))
b = int(input("B: "))
k = 0

for i in range(a, b+1):
    k += 1
    print(i)

print("K = ", k)