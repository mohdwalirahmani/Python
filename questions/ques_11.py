'''
  *
 ***
*****      n=3

'''
num = int(input("Enter the number: "))

for i in range(1,num+1):
    print(" " * (num-i), end="")            #Since end="", the second print() immediately continues on the same line.
    print("*" * (2*i - 1))


''' end="" isse krle se " " or "*" same line m hi print hue

hm ese bhi kr skte the - print(" " * (num - i) + "*" * (2 * i - 1))

'''