# https://www.w3resource.com/python-exercises/python-basic-exercise-49.php
# Python: List all files in a directory in Python

from os import listdir
from os.path import isfile, join

files_list = [f for f in listdir('E:/') if isfile(join('E:/',f))]
print(files_list)
