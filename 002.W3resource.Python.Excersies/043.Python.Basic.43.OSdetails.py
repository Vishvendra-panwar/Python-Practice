# https://www.w3resource.com/python-exercises/python-basic-exercise-43.php

# Write a python program to get OS name, platform and release informations

import platform
import os
print("Name of the Operating System:",os.name)
print("\nName of the OS system:", platform.system())
print("\nVersion of the operating system:",platform.release())