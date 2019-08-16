from genarr import genRandomArr
n = int(input("N: "))

a = genRandomArr(n,-10,10)
print(a)

i = 0
while i < len(a):
    if a[i] < 0:
        a.insert(i+1,0)
        i += 2
    else:
        i += 1

print(a)