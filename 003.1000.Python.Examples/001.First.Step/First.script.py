print ("hello World")

print ("Hello") 
#Comments for other developers

print ("world") # More Comments

# print ("This is not Printed")

# Variables
greeting = "Hello World!!!!!"
print (greeting)

print ("Value Types in python")
print ( type (23) ) # int
print ( type (3.14) ) # float
print ( type ("hello") ) # str
print ( type ("23")) # str
print ( type ("3.14")) # str
print ( type (None)) # NoneType
print ( type (True)) # boole
print ( type (False)) # bool

print ( type ([])) # list
print ( type ({})) # dict

# print ( type (hello)) # NameError: name 'hello' is not defined
print ( "Still running")

print ("Floating Point Limitation")
print (0.1 + 0.2)

## rectangle Area & Circumference

rectangle_width = 23
rectangle_height = 100
rectangle_area = (rectangle_width*rectangle_height)
rectangle_circumference = (rectangle_height + rectangle_width) * 2
print ("Rectangle Ares", rectangle_area)
print ("Rectangle Circumference", rectangle_circumference)

# Circle Area & Circumference

radius = 7
circle_circumference = 2*3.14*radius
print ("Circle circumference is ", circle_circumference)
print ("Circle area is ", 3.14*3.14*radius)


import math

print ("Circle area with math pi ", radius*radius*math.pi)
print ("The Circumference is ", 2*radius*math.pi)