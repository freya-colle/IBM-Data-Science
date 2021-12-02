"""
Week 2:
Hands-On Lab 6: Sets
WHAT TO LEARN: .add, .remove(), &,.intersection(), .difference(), .union(), .issubset(), .issuperset()
"""
'''
SET: a unique collection {} 
        duplicate items: automatically DELETED
REMINDER:
LIST = [] MUTABLE
TUPLE = () IMMUTABLE
DICTIONARY ={} IMMUTABLE

'''

#Create a set
set1 = {"finance", "python", 9, 9, "Freya", "finance", 2, 3}
print('This is my 1st SET:\t', set1)

#CONVERT list to set
list2 = [9, 2, '2', 2.3, "Freya"]
set2 = set(list2)
print('Convert a list to a set:\t', set2)

#SET OPERATIONS
#ADD
set2.add("de")
print('After adding new element:\t',set2)

A = set(["Thriller", "Back in Black", "AC/DC"])
A.add("New")
print('After adding new element:\t',A)

#REMOVE
set2.remove("de")
print('After deleting new element:\t', set2)

#TEST IF THE ELEMENT IS IN THE SET
print('Check if a is in set2:\t','a' in set2)

#SET LOGIC OPERATIONS
album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", 'Back in Black', "The Dark Side of the Moon"])

#INTERSECTION USING &
intersection = album_set1 & album_set2
print('The intersection between 2 diff sets:\t',intersection)
print('The intersection using .intersection:\t',album_set1.intersection(album_set2))

#DIFFERENCES BETWEEN THE TWO SETS
print('The difference in set 2 not set 1:\t',album_set2.difference(album_set1))

#UNION
print('Union of the 2 sets:\t', album_set1.union(album_set2))

#CHECK IF A SET IS SUPERSET OR SUBSET

print(album_set1.issubset(album_set2))
print({"Thriller"}.issubset(album_set1))
print({"a","bc"}.issuperset("a"))