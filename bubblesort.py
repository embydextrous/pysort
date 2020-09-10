# General Complexity of Bubble Sort is O(n^2) however best case complexity can be reduced by terminating outer loop
# if there is no swap in inner loop.
def sort(a):
    n = len(a)
    swapped = False
    for i in range(n):
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        if not swapped:
            break

a = [64, 34, 25, 12, 22, 11, 2]
sort(a)
print a