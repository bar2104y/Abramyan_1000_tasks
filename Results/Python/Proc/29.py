def DigitCount(k):
    cnt = 0
    while k > 0:
        cnt += 1
        k //= 10
    return(cnt)

i = 1
while i <= 1000:
    i+=90
    print(i, DigitCount(i))