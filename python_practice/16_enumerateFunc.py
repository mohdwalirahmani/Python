#enumerate func basically indexing kr deta h jisse programer ko krne ki zrurat na pde

fruits = ['apple', 'mango', 'banana', 'grapes', 'oranges', 'guava', 'pineapple']

#index = 0
#for fal in fruits:
#    print(fal)
#    if (index == 2):
#        print("next is grapes")
#    index += 1

for index, fal in enumerate(fruits):
    print(fal)
    if (index == 4):
        print("Next is guava")

print("\n")
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)