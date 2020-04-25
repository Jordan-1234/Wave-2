#Import library
import math

#Inputs for Quadratic Equation
a = int(input())
b = int(input())
c = int(input())

#First, use the discriminant equation to check for the amount of roots
if b**2 - 4*a*c < 0:
    print("There are no real roots")

#Use the whole quadratics equation to check for the amount roots
else: 
    root1 = int((b*-1 + math.sqrt(b**2 - 4*a*c)) / (2*a))
    root2 = int((b*-1 + math.sqrt(b**2 - 4*a*c)) / (2*a))
    if root1 != root2:
        print("There are 2 real roots")
        print("Root 1 =", root1)
        print("Root 2 =", root2)
    else: 
        print("There is 1 real root. ")
        print("Root 1 =", root1)
