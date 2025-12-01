f = open("01_file.txt", "r")  # This "r" mode is default, it will work even if we don't wirte it
data = f.read()
print(data)
f.close()   

q = open ("04_file.text", "w") # this file doesn't exists initially but if we write this code it will automatically create a file
data = q.read()
print (q)

# we can use "x" to create a file and it will gives us error if that file exists already