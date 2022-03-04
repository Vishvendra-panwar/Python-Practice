# https://www.w3resource.com/python-exercises/python-basic-exercise-37.php
# Write a Python program to display your details like name, age, address in three different lines.

def personal_detail(a,b,c):
    name, age = a,b
    address = c
    print(f"Name: {name} \nAge: {age}\nAddress: {address}")

n1=input("Enter your name : \n")
n2=int(input("Enter your age :\n"))
n3=input("Enter your address :\n")

print(personal_detail(n1,n2,n3))