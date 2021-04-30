import calendar

input_string = input("Enter Month and year in mm/yyyy format\t:")
date = input_string.split("/")
m = int(date[0])
y = int(date[-1])
print ("Printing calendar for month ",m," and year ", y)

print (calendar.month(y,m))