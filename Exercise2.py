"""
Write a Python function that takes a string as an argument
and prints whether it is upper- or lowercase.
"""

def stringcase():
    x = input("Enter a word: ")
    if x.isupper():
        print("UPPER case")
    else:
        print("lower case")

stringcase()