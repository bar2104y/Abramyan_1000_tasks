from genarr import genRandomArr
n = int(input("N: "))

a = genRandomArr(n,2,5)
print(a)

i = 0
while i < len(a)-1:
    if a[i] != a[i+1]:
        a.insert(i+1,a[i])
        i += 1
    i += 1

a.insert(len(a),a[len(a)-1])

print(a)