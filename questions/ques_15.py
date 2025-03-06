# Find sum of n numbers

def sum(n):
    if (n==0):
        return(0)
    return n + sum(n-1)
    # sum(n) calls itself with n-1, breaking the problem down step by step. it is like factorial

n = int(input("Enter the number: "))
print("the sum of the number is: ",sum(n))
