# https://www.w3resource.com/python-exercises/python-basic-exercise-31.php
# Python: Compute the greatest common divisor (GCD) of two positive integers
# Write a Python program to compute the greatest common divisor (GCD) of two positive integers.

# The greatest common divisor (GCD) of two nonzero integers a and b is the greatest positive integer d such that d is a divisor of both a and b; that is, there are integers e and f such that a = de and b = df, and d is the largest such integer. The GCD of a and b is generally denoted gcd(a, b).

# https://www.w3schools.com/python/ref_func_range.asp - Range function

def gcd(x,y):
    gcd = 1
    if x % y == 0:
        return y
    for k in range(int(y / 2), 0, -1):
        if x % k ==0 and y % k == 0:
            gcd = k
            break
    return gcd

n1=int(input("Enter your first number:\n"))
n2=int(input("Enter your Second number:\n"))

print(f"Greatest common divisor (GCD) of {n1} and {n2} is :\n")
print(gcd(n1,n2))