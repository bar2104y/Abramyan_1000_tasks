n = int(input())

l = False
cnt = 0
maxcnt = 0
for i in range(n):
    tmp = int(input())
    if tmp % 2 == 0:
        cnt += 1
        if not l: l = True
    else:
        l = False
        maxcnt = max(maxcnt, cnt)
        cnt = 0

maxcnt = max(maxcnt, cnt)
print(maxcnt)
            
        
