x = int(input("X (kg): "))
a = int(input("A (rub): "))
y = int(input("Y (kg): "))
b = int(input("B (rub): "))

a = a/x
b = b/y

print("1kg first - " +str(a) + " rub")
print("1kg second - " +str(b) + " rub")
print("Price (first/srcond) = " + str(a/b))