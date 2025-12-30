arr = list(map(int, input().split()))
arr2 = []

for i in arr:
    if i not in arr2:
        arr2.append(i)

print(*arr2)
