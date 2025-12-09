'''
map() is a built-in function that applies a function to every item in an iterable (like list, tuple, etc.) and returns a map object (which you can convert to a list).

Think of map() as:
“Take each element → apply a function → give me the results.”

map(function, iterable)  --> Syntax

'''

def cube(x):
    return x*x*x

print(cube(5))

l = [2,4,6,8,10]
#newlist = []
#for i in list:
#    newlist.append(cube(i))

newlist = list(map(cube,l))     # so this is what a map func can do, we don't have to write 7,8,9 line

print(newlist)

#square all no. in a list
sq = map(lambda x:x*x, l)
print(list(sq))

# Add 2 lists element-wise

m = [1,3,5,7,9]
add = map(lambda x,y : x+y, l,m)
print(list(add))

'''
map() works faster than manual loops.
Works great with lambda functions.
'''

# FILTER
# filter(function, iterable)

f = filter(lambda x: x>4, l)
print(list(f))