s = 0.0
a = 1.0

k = int(input())
for i in range(0,k):
    n = float(input())
    s += n
    a *= n

print("+ :",s)
print("* :", a)