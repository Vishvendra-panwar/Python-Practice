# Added "Is" in front of string to given string. 
# If string already have "Is" already in front of strings, don't make changes
def new_String(str):
    if len(str) >= 2 and str[:2] == "Is":
        return str
    return "Is" + str

string = input("Enter String : \t")
print(new_String(string))