"""
Week 3:
Hands-on Lab 8: Loops in Python
    - Range
    - For Loop: REPETITION
    - While Loop: REPETITION UNTIL CONDITIONS MET
note: enumerate
"""
#RANGE
print(range(3))
#For loop
dates = [23, 26, 99, 9]
D = len(dates)

for i in range(D):
    print(dates[i])

for i in range(0,8):
    print(i)

squares = ['red', 'yellow', 'green', 'purple', 'blue']

for i in range(0,5):
    print('Before square', i, 'is', squares[i])
    squares[i] = 'white'
    print('After square', i, 'is', squares[i])

for i, squares in enumerate(squares):
    print('ID - ', i, '; color - ', squares)

#WHILE Loop
names = ['cat', 'dog', 'bird', 'mouse']

d = 0
name = names[0]

while(name != 'bird'):
    print(name)
    d = d + 1
    name = names[d]
print('It took', d, 'repetitions to get out of the loop')

#Quiz
'''Write a while loop to copy the strings 'orange' of the list squares to the list new_squares. 
Stop and exit the loop if the value on the list is not 'orange':'''
squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares =[]
i = 0

while squares[i] == 'orange':
    new_squares.append(squares[i])
    i = i + 1

print(new_squares)



