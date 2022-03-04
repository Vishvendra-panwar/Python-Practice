# https://www.w3resource.com/python-exercises/python-basic-exercise-35.php

# Python Basic: Exercise-35 with Solution
# Write a Python program which will return true if the two given integer values are equal or their sum or difference is 5.

from operator import truediv


def check(x,y):
    if x == y or (x-y) == 5 or (x+y) == 5:
        return True
    else:
        return False

n1=int(input("Enter your first number:\n"))
n2=int(input("Enter your Second number:\n"))

print(f" {n1} and {n2} is :\n")
print(check(n1,n2))