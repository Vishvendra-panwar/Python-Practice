# https://www.w3resource.com/python-exercises/python-basic-exercise-51.php

# Write a Python program to determine profiling of Python programs.
import cProfile
def sum():
    print(1+2)
cProfile.run('sum()')