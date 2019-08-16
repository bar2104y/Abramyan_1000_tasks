from genarr import genRandomArr
n = int(input("N: "))

a = genRandomArr(n,0,5)
print(a)

i = 0
while i < len(a):
    tmp = a[i]
    cnt = 1
    j = i+1
    while j < len(a):
        if a[j] == tmp:
            cnt += 1
        j+=1
    
    if cnt > 2:
        j = i
        while j < len(a):
            if a[j] == tmp:
                a.pop(j)
            else:
                j += 1
    else:
        i += 1

print(a)