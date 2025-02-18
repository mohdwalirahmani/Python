l = [12,"kk",453,"wali","coding","NIET"]


# while loop
i=0
while (i<len(l)):
    print(l[i])
    i += 1

# for loop
for j in l:
    print(j)
else:
    print("done")       #this is printed when loop in exausted

    # The else in a loop only runs if the loop completes without a break.
    # If you simply place a print() statement after the loop, it will run no matter what, even if the loop was terminated with break.


# break statement
for k in range(50):
    if (k == 22):
        break               # it stops the iteration right here
    print(k)

# continue statement
for k in range(50):
    if (k == 22):
        continue               # it skips that iteration
    print(k)