from genarr import genRandomArr
n = int(input("N: "))

a = genRandomArr(n,0,5)
print(a)

b = []

i = 0
while i < len(a):
    tmp = a[i]
    if tmp not in b:
        cnt = 1
        j = i+1
        while j < len(a):
            if a[j] == tmp:
                cnt += 1
            j+=1
        
        if cnt < 3:
            j = i
            while j < len(a):
                if a[j] == tmp:
                    a.pop(j)
                else:
                    j += 1
        else:
            i += 1
    else:
        i += 1
    
    b.append(tmp)

print(a)