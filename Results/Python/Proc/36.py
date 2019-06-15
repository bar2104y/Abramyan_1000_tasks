#1 1 2 3 5 8 13 21 34 55
def Fib(n):
    if n <= 2: return(n)
    f1 = 1
    f2 = 2
    for i in range(n-3):
        tmp = f2
        f2 += f1
        f1 = tmp
    return(f2)

for i in range(101):
    print(Fib(i))