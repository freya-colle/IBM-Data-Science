'''
Week 1
Hands-On Lab 2: Strings
'''

"""
1. Strings: 
    - Use quotation marks, single quotation marks to define
    - Strings include: spaces, digits, special characters  
    - Ordered Sequence: starts at 0  
"""
name = 'Freya Collection' #assign string to variable

"""
2. Indexing
  - Negative Indexing starts at -1 
  - The last element is given by the index -1      
"""
print(name[0]) #F
print(name[-1]) #n
len(name)

"""
3. Slicing
    - Obtain multiple character from string
4. Stride 
"""
name[0:4] #include 0,1,2,3
name[::2] #every second character
name[0:5:2]

"""
5. Concatenate Strings
    - Combine string using +
"""
introduction = "Hello! My name is " + name
introduction

introduction*3 #print 3 times
introduction = introduction + ". Nice to meet you" #create a new string to the original variable

"""
6. Escape Sequence
    \n = Enter
    \t = Tab
    \\ = \
    r with \ = \
"""

print("My name is \nFreya")
print("My name is: \tFreya")
print("My name \\ Freya")
print(r"My name \ Freya")

"""
7. String Operations
    - upper = UPPERCASE
    - replace 
    - find
"""
#upper
print(introduction.upper())
#replace
print(introduction.replace('Freya', 'F'))
#find
name.find('r')
name.find('bniawd') #substring is not in the string, the result will be -1




