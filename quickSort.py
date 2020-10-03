# Time complexity of Quick Sort is O(nLogn) in average and best case while it is O(n^2) in worst case.
# T(n) = T(k) + T(n-k-1) + O(n)
# If Pivot element is first or last and array is sorted asc or desc,
# equation becomes T(n) = T(0) + T(n-1) + O(n) and complexity is O(n^2)
# However, if we pick middle element as pivot, it becomes best case as pivot is always median element.
# T(n) = 2T(n/2) + O(n) --> O(nlogn)

import time
import random

def quickSort(a, l, r):
    if l < r:
        pivot = partition(a, l, r)
        quickSort(a, l, pivot - 1)
        quickSort(a, pivot + 1, r)

# Hoare's Partition - Difficult to Implement
def partition(a, l, r):
    x = random.randrange(1, 50000) % (r - l)
    a[l], a[l+x] = a[l+x], a[l]
    i, j = l + 1, r
    while i <= j:
        while i <= j and a[i] < a[l]:
            i += 1
        while i <= j and a[j] >= a[l]:
            j -= 1
        if i < j:
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    print a
    return j

# Lomuto's Partition - Easy to Implement
def partition2(a, l, r):
    x = random.randrange(1, 50000) % (r - l)
    a[r], a[l + x] = a[l + x], a[r]
    pivot = a[r]
    i = l - 1
    for j in range(l, r):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[r] = a[r], a[i+1]
    print a
    return i+1

# Please refer this - https://cs.stackexchange.com/a/11550

a = [6, 5, 6, 1, 2, 4, 8, 3, 1, 7, 6, 9]

start = time.time() * 1000
quickSort(a, 0, len(a) - 1)
end = time.time() * 1000
print end - start
print a

        