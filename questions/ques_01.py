# write a program to create a dictionary of hindi words with values as their 
# eng character. provide user with as option to look it up

lang = {
    "pyaar" : "Love",
    "bike chalana" : "Riding",
    "ghumna" : "roaming",
    "khelna" : "playing",
    "relationship" : "waste of time"
}
print(type(lang))

a = input("enter the hindi word: ")

print("The Eng translation is " +lang[a])
