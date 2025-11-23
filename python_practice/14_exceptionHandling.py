# if we didn't use exception handling here then if the input may a string then the code shows error and it stops there
# but bcoz of try and except it passed through it showing that there's a error

num = input("Enter a number: ")
print(f"The multiplication table of {num} is: ")

try:
    for i in range(1,11):
        print(f"{int(num)} X {i} = {int(num)*i}")   # if we write int while taking an input, we don't need to mention int here
except:
    print("invalid input")
finally:
    print("I'm always executed")        # y hmesha execute hoga chahe error ho ya na ho

print("This is an imp msg")
print("this is the last line of code")