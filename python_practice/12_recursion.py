'''
factorial (4) = 4x3x2x1
factorial (n) = n* factorial(n-1)

'''

def factorial(n):
    if (n==1 or n==0):
        return(1)
    return n * factorial(n-1)
    # factorial(n) calls itself with n-1, breaking the problem down step by step. 

n = int(input("Enter the number: "))
print("the factorial of the number is: ",factorial(n))

'''

Example Execution (factorial(5)):

factorial(5) = 5 * factorial(4)
factorial(4) = 4 * factorial(3)
factorial(3) = 3 * factorial(2)
factorial(2) = 2 * factorial(1)
factorial(1) = 1 (Base case reached, returns 1)
Now the values return back:

factorial(2) = 2 * 1 = 2
factorial(3) = 3 * 2 = 6
factorial(4) = 4 * 6 = 24
factorial(5) = 5 * 24 = 120
So, factorial(5) = 120.


we didn’t directly tell the computer the factorial formula (n! = n × (n-1) × (n-2) × ... × 1). Instead,
we taught it how to compute it using recursion! The function follows the logic you wrote and computes the result step by step.

'''