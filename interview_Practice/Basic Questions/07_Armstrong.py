n = int(input())
temp = n
digits = len(str(n))
s = 0

while (temp>0):
    s += (temp % 10) ** digits
    temp //= 10

if (n==s):
    print("Armstrong")
else:
    print("Not Armstrong")