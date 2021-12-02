"""
 Week 2
Hands-on Lab: Lists

List: [] a sequenced collection of diff objects (int, str, float, other lists)
        MUTABLE
"""

'''
1. Indexing
'''

L = ["Freya", 25.1, 1996]
print(L)

print('The address of each element within a list is called an index. \n For example: L[0] = L[-3] = ', L[0])
print('the same element using negative and positive indexing: \n Positive:', L[0], '\n Negative:', L[-3])


'''
2. List Content
    str, int, float, other lists, tuples, ...'''
sample_list = ['Freya', 3, 3.2, [3, 9], ('A', 9)]
print('This is the sample list where I nest different data structures inside: \n', sample_list)

'''
3. List Operations: slicing, extend, append, change, delete, split
'''
#SLICING
print('1. SLICING to get the last 2 elements: ', sample_list[3:5])
#EXTEND
sample_list.extend(['22', 99])
print('2. Use EXTEND to add 2 elements to list: \n sample_list.extend(["22", 99]) =', sample_list)
#APPEND
sample_list.append(['22', 99])
print('3. Use APPEND to add 1 element (list): \n sample_list.append(["22", 99]) =', sample_list)
#CHANGE
sample_list[0] = "Freya is beautiful"
print('4. CHANGE the element in list: \n sample_list[0] = "Freya is beautiful" \n', sample_list)
#DELETE
del(sample_list[-1])
print('5. DELETE the last element: \n del(sample_list[-1]) \n', sample_list)
#SPLIT (by defaul split by space) - CONVERT STRING TO LIST
print("6. SPLIT by defaul - space: \n 'Freya is beautiful'.split() \n",'Freya is beautiful'.split())
#SPLIT by comma ,
print("7. CONVERT str to list using SPLIT by comma: \n '2,3,4,d'.split(",") \n", '2,3,4,d'.split(','))

'''
4. Copy and Clone List'''

A = [9, 'nine', 9]
E = A
F = A[:]
print('COPY: \n E = A \n A changes, E changes \n', E)
print('CLONE: \n F = A[:] \n A changes, F WONT change \n', F)


