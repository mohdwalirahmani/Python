age = int(input("Enter the age: "))

if (age%2 == 0):
    print("")


#this is known as if elif else ladder
if (age>=18):
    print("U are eligible for vote")

elif(age<0):
    print("age can't be negative")

elif(age==0):
    print("age must be something other than 0")

else:
    print("bacha h abhi tu")