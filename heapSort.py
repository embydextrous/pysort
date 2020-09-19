# Time complexity of Heap Sort is O(nLogn) in all 3 cases (worst, average and best).
def buildMaxHeap(a):
    n = len(a)
    for i in range(n/2-1, -1, -1):
        maxHeapify(a, n, i)

def maxHeapify(a, n, i):
    largest = i
    l = 2 * i + 1
    r = l + 1
    if l < n and a[l] > a[largest]:
        largest = l
    if r < n and a[r] > a[largest]:
        largest = r
    if i != largest:
        a[largest], a[i] = a[i], a[largest]
        maxHeapify(a, n, largest)

def heapSort(a):
    buildMaxHeap(a)
    for i in range(len(a) - 1, 0, -1):
        a[i], a[0] = a[0], a[i]
        maxHeapify(a, i, 0)
        print a

a = [12, 11, 13, 5, 6, 7]
heapSort(a)
#print a