print("y(x) = 4*(x-3)^6 - 7*(x-3)^3 + 2")
x = int(input("X: "))

y = ((x-3) ** 3) * (4*((x-3)**2) -7) + 2

print("y(" + str(x) + ")= " + str(y) )