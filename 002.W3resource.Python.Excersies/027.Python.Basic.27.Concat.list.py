# Write a Python program to concatenate all elements in a list into a string and return it.
def concatenate_list_data(list):
    result  = ''
    for element in list:
        result += str(element)
    return result

print("Enter your list :\n")
list1=input("->\t")

print("Input veriable is : ", type(list1))
print("User can't give input in List type.")
print("Giving list as input in program hardcoded.")

print(concatenate_list_data(["V","i",]))
print(concatenate_list_data(["M","o","n","i","k","a"]))