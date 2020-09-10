
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
        print a

a = [64, 34, 25, 12, 22, 11, 2]
sort(a)
print a