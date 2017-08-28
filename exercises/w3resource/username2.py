#!/usr/bin/env python
# Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.

first = str(input("Enter your first name:"))
last = str(input("Enter your last name:"))
def fullName(firstName, lastName):
    fullName = firstName + ' ' + lastName
#    print(fullName [::-1])
    print(fullName)

fullName(first,last)
