'''
a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
c = int(input("Enter the number: "))

avg = (a+b+c)/3
print("the average of 3 numbers is: ",avg)

# what if we want to find the average 3 time, then we have to print same code for 3 times

'''
# so here comes funtions, it helps us to do it without making us write a code multiple times

def avg():                                          # funciton definition
    a = int(input("Enter the number: "))
    b = int(input("Enter the number: "))
    c = int(input("Enter the number: "))

    avg = (a+b+c)/3
    print("the average of 3 numbers is: ",avg)

avg()       # function call
avg()
avg()

# we just need to write avg() 3 times for finding avg 3 times


'''
Types of function
1. Build-in func : len(), print(), range(),etc

2. User defined func : jo upr kra

'''
