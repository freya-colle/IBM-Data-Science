"""
Week 4:
Hands-On Lab 14: Writing Files with Open
- write(): save file to a list
3 MODEs: 'r', 'w', 'a'
'w+', 'a+', 'r+
.tell() #return current position in bytes
.seek(offset, from)
 ``r''   Open text file for reading.  The stream is positioned at the
         beginning of the file.

 ``r+''  Open for reading and writing.  The stream is positioned at the
         beginning of the file.

 ``w''   Truncate file to zero length or create text file for writing.
         The stream is positioned at the beginning of the file.

 ``w+''  Open for reading and writing.  The file is created if it does not
         exist, otherwise it is truncated.  The stream is positioned at
         the beginning of the file.

 ``a''   Open for writing.  The file is created if it does not exist.  The
         stream is positioned at the end of the file.  Subsequent writes
         to the file will always end up at the then current end of file,
         irrespective of any intervening fseek(3) or similar.

 ``a+''  Open for reading and writing.  The file is created if it does not
         exist.  The stream is positioned at the end of the file.  Subse-
         quent writes to the file will always end up at the then current
         end of file, irrespective of any intervening fseek(3) or similar.
"""
#Write line to file
ex2 = 'Example2.txt'
with open(ex2, 'w') as writefile:
    writefile.write('This is line D')

#Read file
with open(ex2, 'r') as readfile:
    print('1st read:\n', readfile.read())

#Write multiple lines
with open(ex2, 'w') as writefile:
    writefile.write('This is line E\n')
    writefile.write('This is line F\n')

#Read file
with open(ex2, 'r') as readfile:
    print('2nd read:\n',readfile.read())

Lines = ['This is line A\n', 'This is line B\n', 'This is line C\n']
Lines
#Write the strings in the list to text file
with open('Example2.txt', 'w') as writefile:
    for line in Lines:
        print(line)
        writefile.write(line)

#Read file
with open('Example2.txt', 'r') as readfile:
    print('3rd read:\n', readfile.read())

#w OVERWRITES all the existing data in the file
with open('Example2.txt', 'w') as writefile:
    writefile.write('Overwrite\n')
with open('Example2.txt', 'r') as readfile:
    print('4th read:\n', readfile.read())

#APPENDING FILES
with open(ex2, 'a') as readfile:
    readfile.write('This is line D\n')
    readfile.write('This is line E\n')
    readfile.write('This is line F\n')

#read file
with open(ex2, 'r') as readfile:
    print('5th read:\n', readfile.read())

# a+
with open(ex2, 'a+') as readfile:
    readfile.write('This is line G')
    print(readfile.read()) #nothing appear because of location

# a+
with open(ex2, 'a+') as readfile:
    print('Initial Location: {}'.format(readfile.tell()))

    data = readfile.read()
    if (not data):
        print('Read nothing')
    else:
        print(readfile.read())
    readfile.seek(0,0)
    print(f'New Location: {readfile.tell()}')
    data = readfile.read()
    if (not data):
        print('Read nothing')
    else:
        print(data)
    print('Location after read: {}'.format(readfile.tell()))

# r+ = read and write - beginning of the file
with open(ex2, 'r+') as readfile:
    data = readfile.readlines()
    readfile.seek(0,0) #write at the beginning of the file
    readfile.write('Line1\n')
    readfile.write('Line2\n')
    readfile.write('finished\n')
    readfile.truncate() #delete the old file
    readfile.seek(0, 0)
    print('after add new info and truncate old file:\n',readfile.read())

#Copy a File from Example2.txt to Example3.txt
with open('Example2.txt', 'r') as readfile:
    with open('Example3.txt', 'w') as writefile:
        for line in readfile:
            writefile.write(line)

#Verify if the copy progress works
with open('Example3.txt', 'r') as testfile:
    print(testfile.read())


