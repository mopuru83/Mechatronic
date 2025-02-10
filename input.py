#!/usr/bin/env python

import math
"""
for i in range(0,5):
    name = input ("Enter your name : ")
    age = input ("Enter your age : ")
    print(f"My name is {name} and I am {age} years old")
"""

print("................................................................")
print("         x    |     Cos (x)    |     sin(x)    |     tan (x)     |")
for i in range(-180, 180, 30 ):
    print("................................................................")
    print(f"Angle : {i}  | {math.cos(i)} |  {math.sin(i)} |  {math.tan(i)}  ")
