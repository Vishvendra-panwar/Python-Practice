# https://www.w3resource.com/python-exercises/python-basic-exercise-38.php

# Write a Python program to solve (x + y) * (x + y).

# Test Data : x = 4, y = 3
# Expected Output : (4 + 3) ^ 2) = 49

n1=int(input("Enter your x :\n"))
n2=int(input("Enter your y :\n"))

result = n1*n1 + 2*n1*n1 + n2*n2

print("Solution of (x + y)*(x + y):",result)