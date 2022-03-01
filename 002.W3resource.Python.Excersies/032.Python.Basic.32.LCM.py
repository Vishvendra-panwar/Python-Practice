# https://www.w3resource.com/python-exercises/python-basic-exercise-32.php

# Write a Python program to get the least common multiple (LCM) of two positive integers.

# From Wikipedia,
# In arithmetic and number theory, the least common multiple, lowest common multiple, or smallest common multiple of two integers a and b, usually denoted by lcm(a, b), is the smallest positive integer that is divisible by both a and b. Since division of integers by zero is undefined, this definition has meaning only if a and b are both different from zero. However, some authors define lcm(a,0) as 0 for all a, which is the result of taking the lcm to be the least upper bound in the lattice of divisibility.

def lcm(x,y):
    if x > y:
        z = x
    else:
        z = y
    while(True):
        if((z % x == 0) and (z % y == 0)):
            lcm = z
            break
        z += 1
    return lcm

n1=int(input("Enter your first number:\n"))
n2=int(input("Enter your Second number:\n"))

print(f"least common multiple (LCM) of {n1} and {n2} is :\n")
print(lcm(n1,n2))