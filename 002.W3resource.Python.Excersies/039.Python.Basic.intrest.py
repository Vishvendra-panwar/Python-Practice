# https://www.w3resource.com/python-exercises/python-basic-exercise-39.php

# Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years.

# The formula for future value with compound interest is FV = P(1 + r/n)^nt.
# FV = the future value;
# P = the principal;
# r = the annual interest rate expressed as a decimal;
# n = the number of times interest is paid each year;
# t = time in years.

# Test Data : amt = 10000, int = 3.5, years = 7
# Expected Output : 12722.79"""
principle = float(input("\nEnter your amount: "))
R = float(input("\nEnter your intrest rate: "))
T = float(input("\nEnter your time in years :"))
N = int(input("\nnumber of times interest applied per time period:"))

Amount = principle*(1+(R/100))**(N*T)

print("\nYour Final amount is :", Amount)