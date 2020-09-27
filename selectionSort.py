# Select minimum element and swap it with current element.
# Best, Worst and Average - O(n^2)
def sort(a):
    n = len(a)
    for i in range(n-1):
        minIndex = i
        for j in range(i + 1, n):
            if a[j] < a[minIndex]:
                minIndex = j
        a[minIndex], a[i] = a[i], a[minIndex]

a = [5, 2, 7, 4, 6, 1, 3]
sort(a)
print a
