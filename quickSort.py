# Time complexity of Quick Sort is O(nLogn) in average and best case while it is O(n^2) in worst case.

def quickSort(a, l, r):
    if l < r:
        pivot = partition(a, l, r)
        quickSort(a, l, pivot - 1)
        quickSort(a, pivot + 1, r)

def partition(a, l, r):
    i, j = l + 1, r
    while i < j:
        while i <= r and a[i] <= a[l]:
            i += 1
        while j > l and a[j] >= a[l]:
            j -= 1
        if i < j:
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j

a = [10, 9, 8, 7]
quickSort(a, 0, len(a) - 1)
print a

        