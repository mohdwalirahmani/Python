def greet(name, ending):
    print("Gud Morning", name)
    print(ending)
    
greet("Wali", "Thank u")


def cricket(player):
    print(player, "is a gud player")
    return "Thanks"                     # return nhi likhenge to last m 'none' likha aayega, isme jo likhte h wo a ki jgh aata h

a = cricket("kholi")
print(a)


cricket(input("Enter any player name: "))

# default arguments

def greet(name,ending = "Thank u"):
    print(f"gud day {name}")
    print(ending)

greet("Wali")