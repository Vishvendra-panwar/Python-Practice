# https://www.w3resource.com/python-exercises/python-basic-exercise-30.php
# Write a Python program that will accept the base and height of a triangle and compute the area.

# Python: Area of a triangle

# A triangle is a polygon with three edges and three vertices. It is one of the basic shapes in geometry. A triangle with vertices A, B, and C is denoted triangle ABC.

# formula - Area = 1/2*base*height

b=float(input("Enter base in cm:\n"))
h=float(input("Enter height in cm:\n"))

print("Area of triangle:", b*h/2)