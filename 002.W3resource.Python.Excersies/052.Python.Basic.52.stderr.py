# https://www.w3resource.com/python-exercises/python-basic-exercise-52.php
# Write a Python program to print to stderr.

from __future__ import print_function
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

eprint("abc","efg","xyz",sep="--")