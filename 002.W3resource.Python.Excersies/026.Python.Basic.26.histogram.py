#Write a Python program to create a histogram from a given list of integers.

string=input("Enter you integer strings :\n")

def convert(string):
    list1=[]
    list1[:0]=string
    return list1

list2=convert(string)
print("Your list :", list2)

def histogram( list2 ):
    for n in list2:
        output =" "
        times = int(n)
        while(times > 0):
            output += '*'
            times = times -1
        print(output)
    return 0

print("Your list in histogram :", histogram(list2))