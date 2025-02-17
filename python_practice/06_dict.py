# Dictionary

saima = {
    "name" : "Saima Noor",
    "age" : 9 ,
    "class" : "3rd",
    "Section" : "C",
    "school" : "dsms",
    "grade" : "F+"
}

print(saima["name"])


# dict_methods

print(saima.items())        # y sbko print kr deta h tuple ki form m 

print(saima.keys())

print(saima.values())       # y right hand side waali values ko print kr deta h

saima.update({"grade" : "C", "address" : "okhla vihar"})
print(saima)

print(saima.get("grade"))

print(saima.__len__())