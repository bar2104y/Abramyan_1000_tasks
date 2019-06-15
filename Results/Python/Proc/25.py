import math
def IsSquare(k):
    return( int(bool(math.sqrt(k) % 1 == 0 )))

cnt = 0
for i in range(2,11):
    cnt+= IsSquare(i)
print(cnt)