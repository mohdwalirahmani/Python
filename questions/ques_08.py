# to find weather a number is a prime or not

num = int(input("Enter the number: "))

#for i in range(2,num):
#    if (num%i == 0):
#        print("The number is not a prime number")
#        break
#else:
#    print("The number is a prime number")


# another method
i = 2
while (i<num):
    if (num%i == 0):
        print("The number is not a prime number")
        break
    i += 1
else:
    print("The number is a prime number")