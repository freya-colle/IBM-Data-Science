"""
Week 4:
Hands-On Lab: Reading Files with Open

"""
#Download the Data
import urllib.request
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt'
filename = 'Example1.txt'
urllib.request.urlretrieve(url, filename)
#Reading Text Files
example2 = "Example1.txt"
#OPEN FUNCTION (1ST ARGUMENT: FILE PATH (INCLUDE FILE NAME AND FILE DIRECTORY, 2ND: MODE)
file2 = open(example2, "r")
#print the file name
print('Print the file name = ', file2.name)
print('Print the file mode = ', file2.mode)
#read the file
FileContent2 = file2.read()
print(FileContent2)
type(FileContent2)
#Close the file -> free up resources + ensure consistency
file2.close()
""" A BETTER WAY TO OPEN A FILE"""
with open(example2, 'r') as file2: #with open - auto close
    FileContent = file2.read()
    print(FileContent2)
#verify if the file is closed
file2.closed
with open(example2, 'r') as file2:
    print(file2.read(4))
with open(example2, 'r') as file2:
    print(file2.read(4))
    print(file2.read(4))
    print(file2.read(7))
    print(file2.read(15))

with open(example2, 'r') as file2:
    print(file2.read(16))
    print(file2.read(5))

#READ ONE LINE
with open(example2, 'r') as file2:
    print('first line: ', file2.readline()) #readline() _ read one line

with open(example2, 'r') as file2:
    print('read line: ', file2.readline())
    print('read char: ', file2.read(3))

#ITERATION
with open(example2, 'r') as file2:
    i = 0
    for line in file2:
        print('Iteration ', str(i), ': ', line)
        i = i + 1




