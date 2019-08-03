n = int(input())
last = int(input())

maxsum = 0

for i in range(n-1):
    tmp = int(input())
    maxsum = max(maxsum, last+tmp)

    last = tmp

print("Max sum:",maxsum)