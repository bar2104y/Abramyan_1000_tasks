print("Function y=3x^6 - 6x^2 - 7")
x = int(input("X: "))

r = 3 * x * x * (x ** 3 - 2) - 7
r = str(r)
print("y(" + str(x) + ")= " + r )