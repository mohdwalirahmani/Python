# to find sum of n natural numbers

num = int(input("Enter the number: "))

i = 1
sum = 0

while (i<=num):
    sum += i
    i += 1

print(sum)


# another method
#sum = 0
#for i in range(1,num+1):
#    sum = sum + i
#print (sum)