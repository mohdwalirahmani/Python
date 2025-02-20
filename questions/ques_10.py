# to find the factorial of a given number
# 5! = 1*2*3*4*5

num = int(input("Enter the number: "))

product = 1
for i in range(1,num+1):
    product = product*i

print(f"The factorial of {num} is {product}")