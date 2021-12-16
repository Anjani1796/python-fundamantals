# If you want to run any bash/shell command from the jupyter, you precede by a "!" exclamation mark and write your command
# !cat file_operations(folder name)/file_name

# print(open("C:/Users/anjani.dubey/PycharmProjects/django_project/file_operations/sample.txt"))
# print(open("file_operations/sample.txt")) #shows error
# <_io.TextIOWrapper name='C:/Users/anjani.dubey/PycharmProjects/django_project/file_operations/sample.txt' mode='r' encoding='cp1252'>
# _io.TextIOWrapper - special type of file object

# file = open("C:/Users/anjani.dubey/PycharmProjects/django_project/file_operations/sample.txt")
# print(file.mode) #r to find the mode in which the file is in
#
# #to check file is closed or not
# print(file.closed) #False
# file.close() #to close the file
# print(file.closed) #True
#
# file = open("C:/Users/anjani.dubey/PycharmProjects/django_project/file_operations/sample.txt")
# print(file.read())
# Hello Everyone
# How is everything going!!
# Why do you think I will QUIT!!

# Entire file content available as string


# to move the cursor throughout the file, we us the seek() function, it returns the index at which cursor is currently available

# print(file.seek(0)) #0
# print(file.read(5)) #Hello
#
# print(file.tell()) #5
# # To findn where is the cursor pointing to
#
# print(file.read(5)) # Ever
# # it reads further from the place, cursor was last available at
# print(file.tell()) #10
#
# # again resetting the cursor to the starting position
# print(file.seek(0)) #0
# print(file.read(5)) #Hello
#
# file.seek(0) #Resetting the cursor to the start position
# print(file.readline()) # Hello Everyone
# print(file.readline()) #
# How is everything going!!
# the reason this was printed below, coz one line change i.e. \n present there which made the gap there

# print(file.readline()) #
# Why do you think I will QUIT!!

# file.seek(0)

# print(file.readlines()) #['Hello Everyone\n', 'How is everything going!!\n', 'Why do you think I will QUIT!!']
# list of lines returned as strings


# we should make sure nobody is able to access the file accidentally, so what we do, we always check file is closed or not
# print(file.closed) #False
# file.close()
# print(file.closed) #True

# with open("C:/Users/anjani.dubey/PycharmProjects/django_project/file_operations/sample.txt") as f:
#     data = f.readlines()
#
# print(data) #['Hello Everyone\n', 'How is everything going!!\n', 'Why do you think I will QUIT!!']
# print(file.closed) #True

# when you access a file with the "with" keyword, you don't have to handle the opening and closing of the file, it is handled by "with"


# with open("sample.txt") as f:
#     line = f.readline()
#     while line:
#         print(line)
#         line = f.readline()
"""
Hello Everyone

How is everything going!!

Why do you think I will QUIT!!
"""

# writing to the files
# file = open('example.txt', 'w')  #this created the file if file don't exist and opens the file in case the file is already present
# file.close()
#
# file = open('example.txt', 'w')
# file.write("Lets's check the write operations")
# file.close()

# when a file opened again in write mode, it will overwrite the existing content of the file

# file = open('example.txt', 'w')
# file.write("Lets's check the write operations again")
# file.seek(6)
# file.write(" examine ")
# file.close()


# file = open('example.txt')
# for lines in file:
#     print(lines)
# Lets's examine e write operations again

# with open('example.txt', 'w') as f:
#     f.write('First line\n')
#     f.write('Second line\n')
#     f.write('Third line\n')
# this code will enter these lines into the file
# and because we are opening the file using the with block that's why, it will open and close the file on its own

# you need to open the file in append mode and hence we can add content to an existing file without over writing

# f = open("example.txt", 'a')
# print(f.tell())
# f.writelines(['Another line was appended\n',
#               'What will it look like now!\n',
#               'Lets check it out\n'])
# f.close()
#
# f = open("example.txt")
# print(f.readlines())
#
# print(f.fileno()) #3
# # it tells the file descriptor used by the operating system to identify the file
#
# print(f.isatty()) #False
# # tells whether the file is attached to some terminal device
#
# print(f.readable()) #True
#
# print(f.writable()) #False because file opened in read mode

# The r+ and a+ mode in file operations

# f = open('example.txt', 'a')
# # opening the file in append mode will always take the cursor to the end of file
# print(f.tell()) #112 - consisting of six lines

# to ensure the file cursor is exactly at the end of the file, you can make use of the "os" module and us e the below code to find the size
# import os
# print(os.stat("example.txt").st_size) #112
# it returned the same file hence we can say that the file is the 112 size big.

# f = open('example.txt', 'r')
# print(f.readlines())
# ['First line\n', 'Second line\n', 'Third line\n', 'Another line was appended\n', 'What will it look like now!\n', 'Lets check it out\n']
# contents of the file

# in order to restrict the file size to some character,  we use the truncate function to put the file size restriction
# f.truncate(37)
# here we restrict size to 37 which means the first 37 characters will remain in the file and rest all will be deleted

# f = open('example.txt', 'r')
# print(f.readlines())
# ['First line\n', 'Second line\n', 'Third line\n']
# truncate function deleted the characters after the 37 character

# when you open the file in the r+ mode, you can3 read as well as write to the file and cursor will point to the beginning of the file


# f = open('example.txt', 'r+')
# f.writelines('We are doing an r+ operation')
# print(f.readlines())
# f.close()
# ['We are doing an r+ operationrd line\n']

# here the writelines() function has overwritten the existing content of the file and some part of previous content is still present

# we are trying to write the bigger text so it replaces the complete older text

# f = open('example.txt', 'r+'))
# f.writelines('In r+ mode, the cursor is initially at the start of the file and use seek to relocate cursor')
# f.close(

"""
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

# a+ mode means reading and appending, cursor at the end of file

# f = open("example.txt", 'a+')
# f.writelines("\nWhat does writing in a+ do?")
# f.close()

# RENAMING an existtng file
# import os
# os.rename('example+name_changed', 'example+name_changed.txt')
# this renamed the file name from the example+name_changed to example+name_changed.txt

# To remove a file
# import os
# os.remove('example+name_changed.txt')
# # this deleted the file