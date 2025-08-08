from lib2to3.pgen2.grammar import opmap_raw
from operator import index

file = open("index.txt","r")
print(file.read())
#You can return one line by using the readline() method:
# print(file.readline())

#Return the 5 first characters of the file:
with open("index.txt") as f:
    print("5 characters are ",f.read(5))

# Loop through the file line by line:
print("looping")
with open("index.txt") as f:
    for x in f:
        print(x)


#wrting to a file
# To write to an existing file, you must add a parameter to the open() function:
#
# "a" - Append - will append to the end of the file
#
# "w" - Write - will overwrite any existing content

#write operation
# print("file 2 contenets are ")
# file2 = open("index.txt" , "w")
# file2.write("dfsadfwefwefdsfsdf")
# file_3 = open("index.txt","r")
# print(file_3.read())


#append operation
file_append = open("write.txt" , "a")
file_append.write(" this is append text")
file4 = open("write.txt","r")
print(file4.read())



