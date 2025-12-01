str = "hey, my name is Mohd Wali"

f = open("02_file.txt", "w")    # y sirf likhega aur agr baar baar ise run krenge to overwrite kr dega aur sirf ek hi baar write hoga

# f = open("02_file.txt", "a")    # y append kr dega, jitni baar chalaoge utni baar write krta jayega

f.write(str)
f.close()

with open("02_file.txt", "a") as f:
    f.write("\nNow I'm using 'with'")

# using 'with' we don't have to close the file