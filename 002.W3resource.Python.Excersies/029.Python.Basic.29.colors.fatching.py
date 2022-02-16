# https://www.w3resource.com/python-exercises/python-basic-exercise-29.php

# Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2.

# Test Data:
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
# Expected Output :
# {'Black', 'White'}

def Diff(list1,list2):
    return list(set(list2) - set(list1))

cl1=input("Please Enter your First colour list with comma seperation:\t")
cl2=input("Please Enter your Second Colour list with comma seperation:\t")

list1=cl1.split(",")
list2=cl2.split(",")

print("List 1 = \n", list1)
print("List 2 = \n", list2)

print("\n Printing colour which are not in part of Colour list1 and present Colour list2:")
# print(list1.difference(list2)) -- Not working
print(Diff(list1,list2))

print("\n Printing colour which are not in part of Colour list2 and present Colour list1:")
# print(list2.difference(list1)) -- Not working
print(Diff(list2,list1))