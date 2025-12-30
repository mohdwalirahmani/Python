arr = list(map(int, input().split()))

largest = arr[0]
smallest = arr[0]

for i in arr:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i

print(largest, smallest)