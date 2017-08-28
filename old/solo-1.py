#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      wk186012
#
# Created:     29-10-2016
# Copyright:   (c) wk186012 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

while True:
    print("Enter 'add' to add numbers")
    print("Enter 'subtruct' to subtruct numbers")
    print("Enter 'divide' do divide numbers")
    print("Enter 'multiple' to multiple numbers")
    user_input = input(":")

    if user_input == "quit":
        break
    elif user_input == "add":
        num1 = float(input("Enter a first number:"))
        num2 = float(input("Enter a second number:"))
        result = str(num1+num2)
        print("The answer is" +result)
    elif user_input == "subtruct":
        num1 = float(input("Enter a first number:"))
        num2 = float(input("Enter a second number:"))
    elif user_input == "divide":
        num1 = float(input("Enter a first number:"))
        num2 = float(input("Enter a second number:"))
    elif user_input == "multiple":
        num1 = float(input("Enter a first number:"))
        num2 = float(input("Enter a second number:"))