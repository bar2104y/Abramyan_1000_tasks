a = int(input("N: "))

f1 = 1
f2 = 1
print(f2)
print(f1)

for i in range(0,a-2):
    f = f1+f2
    f2 = f1
    f1 = f
    print(f)