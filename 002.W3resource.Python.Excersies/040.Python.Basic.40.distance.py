# https://www.w3resource.com/python-exercises/python-basic-exercise-40.php

# Python Basic: Exercise-40 with Solution
# Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).
# pip install geopy

import geopy.distance

lat1 = float(input("\nEnter your First latitude : "))
lon1 = float(input("\nEnter your First longitude : "))
lat2 = float(input("\nEnter your Second Latitude : "))
lon2 = float(input("\nEnter your Second longitude : "))

coordinate_1 = (lat1,lon1)
coordinate_2 = (lat2,lon2)

print (geopy.distance.geodesic(coordinate_1,coordinate_2).km)