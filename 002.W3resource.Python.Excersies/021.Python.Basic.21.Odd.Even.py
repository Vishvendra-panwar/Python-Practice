# 21. Write a Python program to find whether a given number from the user
# is even or odd, print out an appropriate message to the user.

no=int(input("Enter your no. : \t"))
mod= no%2
if mod == 0:
    print(" ", no, " is an even number.")
else:
    print(" ", no, " is an odd number.")