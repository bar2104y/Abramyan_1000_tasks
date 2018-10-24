a = 1.0

k = int(input())
for i in range(0,k):
    n = float(input())
    d = n - int(n)
    print(i+1,":",d)
    a *= n

print("Mtply :",a)