# https://www.w3resource.com/python-exercises/python-basic-exercise-46.php
# Python: Get the path and name of the file that is currently executing
# Write a python program to get the path and name of the file that is currently executing.

import os
print("Current File Name :",os.path.realpath(__file__))