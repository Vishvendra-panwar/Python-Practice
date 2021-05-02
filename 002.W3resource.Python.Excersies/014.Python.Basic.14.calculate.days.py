from datetime import date

one = input("Enter first date in DD/MM/YYYY format:\t\n")
two = input("Enter second date in DD/MM/YYYY format:\t\n")

date1 = one.split("/")
date2 = two.split("/")

f_date = date(int(date1[-1]),int(date1[1]),int(date1[0]))
l_date = date(int(date2[-1]),int(date2[1]),int(date2[0]))

dalta = l_date - f_date
print("dalta days :", dalta.days)