"""
Week 3:
Hands-On Lab 9: Functions
"""

'''
There are two types of functions :
(1) Pre-defined functions
(2) User defined functions'''

#First function example:

def add(a):
    """ add 1 to a"""
    b = a + 1
    print(a, 'if you add one', b)
    return(b)

print(add(2))

def multi(d,e):
    t = d*e
    return(t)

result2 = multi(12,2)
print(result2)

def square(u):
    o = 1
    n = u*u + o
    print(u, 'if you square + 1', n)
    return(n)

print(square(3))

def MJ():
    print('Michael Jackson')
MJ()
def MJ1():
    print('Michael Jackson')
    return(None)

print(MJ1())

def combine(a, b):
    return(a + b)

print(combine('Freya ', 'Python'))

x = int(input('x = ',))
y = square(x)
print(y)

square(2)

#FUNCTIONS MAKE THINGS SIMPLE
a1 = 4
b1 = 5
c1 = a1 + b1 + 2*a1*b1-1
if (c1<0):
    c1 = 0
else:
    c1 = 5
print('c1 = ', c1)

def Equation(a, b):
    c = a + b + 2*a*b - 1
    if (c <0):
        c = 0
    else:
        c = 5
    return(c)
print('Equation = ', Equation(4,5))

###PREDEFINED FUNCTION: print(), sum(), len()
album_ratings = [2, 3, 4, 5, 8, 9]
print(album_ratings)
sum(album_ratings)
len(album_ratings)

###IF/ ELSE STATEMENT
def type_of_album(artist, album, year_released):
    print(artist, album, year_released)
    if year_released > 1980:
        return 'Mordern'
    else:
        return 'Oldie'
x = type_of_album("Michael Jackson", "Thriller", 1980)
print(x)

#Print element in list:
def Printlist(list23):
    for element in list23:
        print(element)
Printlist([2,3,4,5])

###SET DEFAULT ARGUMENT VALUES IN CUSTOM FUNCTIONS
def isGoodRating(rating = 4):
    if rating <7 :
        print('This album sucks, rating is ', rating)
    else:
        print('This album is good, rating is ', rating)

isGoodRating()
isGoodRating(22)

###Global variables
artist = 'Freyaa'
def printer2(artist):
    internal_var = artist #local var
    print(artist, 'is an artist')
printer2(artist)
printer2(internal_var) #NameError 'internal_var' is NOT defined
printer2('ADELE')
def printer3(artist):
    global internal_var
    internal_var = '???'
    print(artist, 'is an artist')

printer3(artist)
printer3(internal_var)



