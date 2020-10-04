import random

def quickSort(a, l, r):
    if l < r:
        p = partition(a, l, r)
        quickSort(a, l, p[0] - 1)
        quickSort(a, p[1] + 1, r)

def partition(a, l, r):
    i = m = l
    j = r - 1
    pivot = a[r]
    while m <= j:
        if a[m] == pivot:
            m += 1
        elif a[m] < pivot:
            a[m], a[i] = a[i], a[m]
            i += 1
            m += 1
        else:
            a[m], a[j] = a[j], a[m]
            j -= 1
    a[m], a[r] = a[r], a[m]
    return (i, m)

a = []
for i in range(100):
    a.append(random.randrange(1, 6))
print a
quickSort(a, 0, len(a) - 1)
print a