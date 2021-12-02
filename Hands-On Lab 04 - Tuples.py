"""
Week 2:
Hands-On Lab 4: Tuples
"""

'''
Tuples: IMMUTABLE ()

'''

#CREATE MY FIRST TUPLE
tuple2 = ("finance", 25, 92)
print('This is my first tuple:\t',tuple2, '\ntype: ', type(tuple2))

#INDEXING
print('Get the index 2 of tuple2:\t', tuple2[2], '\nCheck the type:\t', type(tuple2[2]))

#CONCATENATE and SLICING
tuple3 = tuple2 + ('good morning', 'fighting', '5')
print(tuple3)
print(len(tuple3))
print(tuple3[3:5])

#SORTING
Ratings = (9,5,4, 2, 8)
f = sorted(Ratings)
print(f)

#NESTING
NestedT =(1, 2, ("pop", "rock") ,(3,4),("disco",(1,2)))
print('Get the first element of the index 2 of NestedT:\t', NestedT[2][0])
print('Get the first element of the 2nd element in the 2nd nested tuples:\t', NestedT[2][1][0])


