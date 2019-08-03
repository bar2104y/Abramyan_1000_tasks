m = int(input())

l = False
cnt = 0
s = 0
maxcnt = 0

for i in range(m):
    tmp = int(input())
    if tmp:
        cnt += 1
        if not l:
            s = i+1
            l = True
    else:
        if cnt >= maxcnt:
            ls = s
            maxcnt = cnt
        cnt = 0
        l = False

if cnt >= maxcnt:
    ls = s
    maxcnt = cnt

print("Start", ls, "; Cnt is", maxcnt)