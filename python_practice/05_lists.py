random = ["bleh", "blooh",45, 65, False,"lapi"]

print(random)
random[1] = "blah"      # lists are mutable unlike strings
print(random)

random.append("one more")
print(random)


l1 = [5,55,68,12,3,12,57,82]
print(l1)

# l1.sort()
# print(l1)

l1.reverse()
print(l1)

l1.insert(3,99)        #this will add 99 on 3rd place
print(l1)

l1.pop(2)   #delete index at number 2
print(l1)

l1.remove(99)           # this will remove 99 from the list
print(l1)