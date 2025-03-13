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