#не работает
a = [0,1,2,3,4,5]
n = len(a)
j = 0

#!!!!!!!!!!!!!!
#!!!ВНИМАНИЕ!!!
#!!!КОСТЫЛИ!!!!
#!!!!!!!!!!!!!!
for i in range((n+3)//4):
    if j in range(n):
        print(a[j])
        if j+1 in range(n):
            print(a[j+1])
            if n-1-j in range(n):
                print(a[n-1-j])
                if n-2-j in range(n):
                    print(a[n-2-j])
    j+=2