num = input("Enter the number between 10 and 15: ")

#if user wants to quit then we do this
if num.lower() == "quit":
    exit()

n = int(num)
if (n<10 or n >16):
    raise ValueError("u have to write number bt 10-15, dumbass")
else:
    print("great")
