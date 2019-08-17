from genarr import genRandomArr
n = int(input("N: "))

a = genRandomArr(n,2,5)
print(a)

i = 0
while i < len(a)-1:
    if a[i] != a[i+1]:
        a.pop(i)
        i -= 1
    i += 1
#     print(a)

a.pop(len(a)-1)

print(a)