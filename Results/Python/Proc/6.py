
c = 0
s = 0

def DigitCountSum(k):
    global c
    global s

    while k>0:
        c += 1
        s += k % 10
        k //= 10

for i in range(0,5):
    DigitCountSum(int(input()))

print('Sum', s)
print("Count", c)

        


