m = int(input())

cnt = 0
n = 0
num = 0
maxcnt = 0
ln = 0
minn = 10000

for i in range(m):
    tmp = int(input())
    if tmp == num:
        cnt += 1
    else:
        if num < minn:
            if cnt > maxcnt:
                ln  = n
                maxcnt = cnt
            n = i+1
            cnt = 1
            num = tmp

if cnt > maxcnt:
    ln  = n
    maxcnt = cnt

print("Start", ln, "; Cnt is", maxcnt)