# Write a Python program to check whether a specified value is contained in a group of values.

#Test Data:
#3 -> [1, 5, 8, 3] : True
#-1 -> [1, 5, 8, 3] : False

print("!!!! i have a Secret No. !!!!\t\n")
print("!!!! Guess my Secret No. and furtune will favor you !!!!\t\n")
guess=int(input("Enter No. here ->"))
secret_list=[13,7,3,1,80085]

def is_guess_correct(secret_list,guess):
    for value in secret_list:
        if guess == value:
            return "I love you Laddo <3"
    return "Try Again"

print(is_guess_correct(secret_list, guess))
