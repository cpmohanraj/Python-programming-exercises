'''
Question 5
Level 1

Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters


'''


class InOutString(object):
    def __init__(self):
        self.str = "No Input Given"

    def getString(self):
        self.str = input("Type something")

    def printString(self):
        print(self.str)

tst = InOutString()
tst.getString()
tst.printString()