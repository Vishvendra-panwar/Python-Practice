string=input("Your Strings :\t")
times=int(input("How many times you want to repeat : \t"))
result = ""
for i in range(times):
    result = result + string

print("New String : \n",result)