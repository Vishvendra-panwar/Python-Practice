# Write a Python program to count the number 4 in a given list.

def list_count_4(nums):
  count = 0  
  for num in nums:
    if num == 4:
      count = count + 1
    
  return count

print(list_count_4([1, 4, 6, 7, 4]))
print(list_count_4([1, 4, 6, 4, 7, 4]))

#no=int(input("Enter your no.:"))
#print(type(no))

#number=str(no)
#print(type(number))

#print(len(number))

#print("Count of digit 4 in entered No.:", list_count_4(number))



