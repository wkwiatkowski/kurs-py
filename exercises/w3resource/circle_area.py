#!/usr/bin/env python
# Write a Python program which accepts the radius of a circle from the user and compute the area.

import math

r = float(input("Please enter a radius of a circle: "))
a = math.pi * r **2

print
print("A area of circle is: " + str(a))

print("\nOr\n")

print ("The area of the circle with radius " + str(r) + " is: " + str(math.pi * r**2))
