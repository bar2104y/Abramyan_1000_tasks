def DigitCount(k):
    cnt = 0
    while k > 0:
        cnt += 1
        k //= 10
    return(cnt)

def DigitN(k,n):
    for i in range(n):
        d = k % 10
        k //= 10
    return(d)

def IsPalendrome(k):
    cnt = DigitCount(k)
    for i in range(1,cnt//2+1):
        if DigitN(k, i) != DigitN(k,cnt-i+1):
            return(False)
    return(True)

a = int(input())
print(IsPalendrome(a))
