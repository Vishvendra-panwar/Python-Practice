# https://www.w3resource.com/python-exercises/python-basic-exercise-44.php

# Write a Python program to locate Python site-packages.

# site.getsitepackages(): Return a list containing all global site-packages directories.

import site
print(site.getsitepackages())
print(site.getusersitepackages())