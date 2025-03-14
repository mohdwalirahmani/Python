f = open("03_file.txt")

''' 
lines = f.readlines()

print(lines)
print(type(lines))

f.close()
'''

lines = f.readline()

while (lines != ""):
    print(lines)
    line = f.readline()

f.close()

# y loop m chale ja rha h, idk kese shi hoga

'''
modes-
r - to read the content from file
w - to write the content into file
a - to append the existing content into file
r+:  To read and write data into the file. The previous data in the file will be overridden.
w+: To write and read data. It will override existing data.
a+: To append and read data from the file. It won’t override existing data.

'''