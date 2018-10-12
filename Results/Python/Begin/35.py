v = int(input("V Boat:  "))
u = int(input("V River: "))
t1 = int(input("T lake:  "))
t2 = int(input("T river: "))

s = v*t1 + t2*(v-u)

print("S =",s)