# sets are unordered
# they are unindexed
# there is no way to change items in sets
# cannot contains duplicate tems

s = {12,24,5,35,6,55,5,5,5,"blooh"}        #no repetition allowed in sets

print(set,type(s))
s.add("bleh")

print(s)
print(len(s))

a=set()
a.add(20)
a.add("20")
a.add(20.00)

print(a)
print(len(a))