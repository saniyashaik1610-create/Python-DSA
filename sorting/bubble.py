a = [2, 4, 7, 1, 3, 6, 5, 8]

for i in range(7):
    for j in range(7 - i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print("Sorted array:", a)