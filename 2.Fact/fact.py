#
# This is a comment
#

"""
This is a comment
"""


'''
Another comment
'''

def inputNumber(message):
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print("Not an integer! Try again.")
        else:
            return userInput

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

number = inputNumber("Please enter a number: ")
print("Fact result is :", fact(number))