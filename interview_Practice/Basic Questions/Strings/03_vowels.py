s = input()
vowels = consonents = digit = 0

for char in s:
    if char.lower() in "aeiou":
        vowels += 1
    elif char.isalpha():
        consonents += 1
    elif char.isdigit():
        digit += 1

print(vowels)
print(consonents)
print(digit)