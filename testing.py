"""
#program to check the given number is even
n = int(input("enter the value of A: "))
if n%2 == 0:
    print(n," is an even number")
else:
    print(n," is not an even number")

#prigram to swap the variables
x = int(input("Enter the value of a"))
y = int(input("Enter the value of b"))
temp = x
x = y 
y = temp
print("the value of x after swap: ",x)
print("the value of y after swap: ",y)
"""
from math import pi


r = int((input("enter the radius of the circle: ")))
R = r*r
print(R)
AREA = pi*R
print("AREA OF THE CIRCLE  IS : ",AREA)
