"""
Week 3:
Hands-On Lab 11: Objects and Classes
1. Create a Class (Attribute, Method)
 - METHODS: change and interact with object
2. Instances of a Class: Objects and Attributes

"""
import matplotlib.pyplot as plt

#REVIEW ABT FUNCTIONS
def add(a, b):
    return (a + b)
a = float(input('ADD FUNCTION a = ', ))
b = float(input('ADD FUNCTION b = ', ))
print('ADD FUNCTION a + b = ', add(a,b))

#CREATE a Point Class
class Points(object):
    def __init__(self, x, y): #TypeError: object() take no argument when NOT define __init__
        self.x = x
        self.y = y
    def print_point(self):
        print('x = ', self.x, 'y = ', self.y)

p2 = Points(1,2)

p2.x = 'A'

p2.print_point()

#CREATE THE CLASS CIRCLE

"""class Circle(object):

    # Constructor
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color

    # Method
    def add_radius(self, r):
        self.radius = self.radius + r
        return (self.radius)

    # Method
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()"""

class Circle():
    #Constructor
    def __init__(self, radius, color): #data attributes: radius, color
        self.radius = radius
        self.color = color
    #Method
    def print_Circle(self):
        print('radius = ', self.radius, '- color = ', self.color)
    def add_Circle(self, r):
        self.radius = self.radius + r
        return(self.radius)
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0,0), radius = self.radius, fc = self.color))
        plt.axis('scaled')
        plt.show()

c2 = Circle(3, 'purple')
c2.print_Circle()
c2.drawCircle()
print(dir(Circle)) #dir() to check METHODS used

RedCircle = Circle(1, 'red') #Create the RedCircle
print('This is the radius of RedCircle: ', RedCircle.radius)
x = int(input('x = ', ))
print('This is the radius of RedCircle after add_radius(x):', RedCircle.add_Circle(x))


class rectangle():
    #data attributes: color, height, width
    def __init__(self, height, width, color):
        self.height = height
        self.width = width
        self.color = color
    def print_rectangle(self):
        print('height = ', self.height, '\nwidth = ', self.width, '\ncolor = ', self.color)
    def draw_rectangle(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), self.height, self.width, fc = self.color)) #to get the current Axes
        plt.axis('scaled')
        plt.show()

rec23 = rectangle(2, 3, 'green')
rec23.print_rectangle()
rec23.draw_rectangle()

