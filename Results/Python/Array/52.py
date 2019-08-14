from genarr import genRandomArr
n = int(input("N: "))

a = genRandomArr(n,0,10)
print(a)

b = []

for i in a:
    if i < 5:
        b.append(2*i)
    else:
        #b.append(i/2)
        b.append(int(i/2))


print(b)