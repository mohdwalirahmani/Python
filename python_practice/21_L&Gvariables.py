x = 45

def my_func():
    global x
    x = 56
    y = 74
    print(x)
    print(y)

print (x)   # it prints 45
my_func()
print (x)   # this gives 56

# print (y) #error bcoz it is local variable and it can be print inside a func only