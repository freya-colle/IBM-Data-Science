"""
Week 1
Hands-On Lab 1 : Your First Program, Types, Expressions, and Variables
"""
""" This is how to write multi-line comment.
1. Your first program and print() statement
"""
print('Hello, World!')

#Check the Python version
import sys
print(sys.version)

"""
2. Types of objects in Python
     strings    integers    floats   boolean 
     Note: // is int division
"""
print(type(12))  #int
print(type(3/3)) #float
print(type(3//3)) #int
print(type('FREYA')) #str
print(type(True)) #bool
print(type(False)) #bool

#System settings about float type
print(sys.float_info)

#Convert one type to another
float(2)
int(3.2)
int('12')
str(2)
bool(1)
bool(0)
float(True)

'''3. Expression and Variables'''
a = 9 + 9
print(a)
print(9 - 3)
print(25/5)
print(25//6)

'''4. Errors in Python: NameError, SyntaxError, ValueError'''
print('1st error is the NameError: \t frint(abc) \t print not frint')
print('2nd error is the Suntax Value: \t int("1 or 2") \t we can not convert characters into int')
print('3rd error is the Value Error: \t print(Hello") \t print("Hello") not print(Hello")')






