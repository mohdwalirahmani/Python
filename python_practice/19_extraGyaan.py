'''
 __name__ == "__main__"
it ensures code runs only when the file is executed directly, not when imported.
'''

def add(a,b):
    return a+b

print("This will always print")

if __name__ == "__main__" :
    print(add(5,10))

'''
if we run this directly then the output will be...
This will always print
15
but, if we import this file that is extraGyaan.py in some other file then the function inside __name__ == "__main__" will not run.
so we use this if we don't want that some other file will use our func by importing
'''