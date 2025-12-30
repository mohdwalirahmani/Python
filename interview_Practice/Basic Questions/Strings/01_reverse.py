s = input()
rev = ""

for char in s:
    rev = char + rev

print(rev)

print(s[::-1])