# Time complexity of Merge Sort is O(nLogn) in all 3 cases (worst, average and best) as merge sort always divides the array into two halves and take linear time to merge two halves.
def mergeSort(a):
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

a = [12, 11, 13, 5, 6, 7]
print mergeSort(a)
print a



