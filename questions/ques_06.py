# wap to find out wheather a given statement is talking about me or not

name = input("Enter the name: ")
statement = input("Enter the statement: ")

#if (name in statement):
#    print("ur name is in the statement")
#else:
#    print("ur name is not in the statement")


if (name.lower() in statement.lower()):
    print("ur name is in the statement")
else:
    print("ur name is not in the statement")

# .lower isliye likhe h kyuki agr naam small m hua aur statement upper m dikkat aayegi.