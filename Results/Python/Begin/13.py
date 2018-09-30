import math
print("R1 > R2")
r1 = int(input("R1: "))
r2 = int(input("R2: "))

s1 = math.pi * r1 * r1
s2 = math.pi * r2 * r2
s3 = str( s1 - s2 )

print( "S1 = " + str(s1) )
print( "S2 = " + str(s2) )
print( "S3 = " + s3 )