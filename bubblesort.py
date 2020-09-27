# General Complexity of Bubble Sort is O(n^2) however best case complexity can be reduced by terminating outer loop
# if there is no swap in inner loop.
def sort(a):
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        if not swapped:
            break

def recursiveBubbleSort(a, l, r):
    n = (r - l) + 1
    if n > 1:
        isSwapped = False
        for i in range(l, r):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                isSwapped = True
        if isSwapped:
            recursiveBubbleSort(a, l, r - 1)


a = [64, 34, 25, 12, 22, 11, 2]
recursiveBubbleSort(a, 0, len(a) - 1)
print a