# Time complexity of Quick Sort is O(nLogn) in average and best case while it is O(n^2) in worst case.
# T(n) = T(k) + T(n-k-1) + O(n)
# If Pivot element is first or last and array is sorted asc or desc,
# equation becomes T(n) = T(0) + T(n-1) + O(n) and complexity is O(n^2)
# However, if we pick middle element as pivot, it becomes best case as pivot is always median element.
# T(n) = 2T(n/2) + O(n) --> O(nlogn)

def quickSort(a, l, r):
    if l < r:
        pivot = partition(a, l, r)
        quickSort(a, l, pivot - 1)
        quickSort(a, pivot + 1, r)

def partition(a, l, r):
    i, j = l + 1, r
    while i <= j:
        while i <= j and a[i] <= a[l]:
            i += 1
        while i <= j and a[j] >= a[l]:
            j -= 1
        if i < j:
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j

def partition2(a, l, r):
    pivot = a[r]
    i = l - 1
    for j in range(l, r):
        if a[j] < pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[r] = a[r], a[i+1]
    return i+1

a = [1, 2, 2, 3, 2, 1, 0, 3, 2, 1]
quickSort(a, 0, len(a) - 1)
print a

        