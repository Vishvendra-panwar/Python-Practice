# https://www.w3resource.com/python-exercises/python-basic-exercise-36.php

# Python: Add two objects if both objects are an integer type

def sum_numbers(a,b):
    if not (isinstance(a,int) and isinstance(b, int)):
        return "Error: Inputs must be integers!"
    return a + b

n1 = input("Enter First No.:\n")
print(type(n1))
n2 = input("Enter Second No.:\n")
print(type(n2))

print (sum_numbers(n1, n2))