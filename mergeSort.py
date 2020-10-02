# Time complexity of Merge Sort is O(nLogn) in all 3 cases (worst, average and best) as merge sort always divides the array into two halves and take linear time to merge two halves.
def mergeSort(a):
    if len(a) > 1:
        mid = len(a) / 2
        L = a[:mid]
        R = a[mid:]
        mergeSort(L)
        mergeSort(R)

        i, j, k = 0, 0, 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                a[k] = L[i]
                i += 1
            else:
                a[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            a[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            a[k] = R[j]
            j += 1
            k += 1

def mergeSort2(a):
    if len(a) > 1:
        mid = len(a) / 2
        L = a[:mid]
        R = a[mid:]
        L = mergeSort(L)
        R = mergeSort(R)
        a = []

        while len(L) > 0 and len(R) > 0:
            if L[0] < R[0]:
                a.append(L.pop(0))
            else:
                a.append(R.pop(0))
        a += L
        a += R
    return a

def mergeSortIterative(a):
    currentSize = 1
    while currentSize < len(a) - 1:
        left = 0
        while left < len(a) - 1:
            mid = min(left + currentSize - 1, len(a) - 1)
            right = min(left + 2 * currentSize - 1, len(a) - 1)
            merge(a, left, mid, right)
            left += 2 * currentSize
        currentSize *= 2

def merge(a, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [-1] * n1
    R = [-1] * n2
    for i in range(n1):
        L[i] = a[l+i]
    for i in range(n2):
        R[i] = a[m+1+i]
    i = j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1
        k += 1
    
    while i < n1:
        a[k] = L[i]
        k += 1
        i += 1
    
    while j < n2:
        a[k] = R[j]
        k += 1
        j += 1


a = [12, 11, 13, 5, 6, 7]
mergeSortIterative(a)
print a



