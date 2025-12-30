arr = list(map(int, input().split()))

largest = max(arr)
second = -1

for i in arr:
    if i != largest and i > second:
        second = i

print(second)

# not giving right output