from genarr import genLinearArr
n = int(input("N: "))

a = genLinearArr(n)
print(a)

i = 0
while i < len(a):
    if a[i] % 2 == 1:
        a.insert(i,a[i])
        a.insert(i, a[i])
        i += 3
    else:
        i += 1

print(a)