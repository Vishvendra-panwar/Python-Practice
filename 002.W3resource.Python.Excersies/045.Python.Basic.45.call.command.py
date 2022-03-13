# https://www.w3resource.com/python-exercises/python-basic-exercise-45.php

# Write a python program to call an external command in Python.

import subprocess
import os

subprocess.call('ipconfig',shell=True)
print(os.system('dir'))