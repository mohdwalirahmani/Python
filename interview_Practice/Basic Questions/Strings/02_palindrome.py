s = input()
rev = ""

for char in s:
    rev = char + rev

if s == rev:
    print("Palindrome")
else:
    print("Not Palindrome")