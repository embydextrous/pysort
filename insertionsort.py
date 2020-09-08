def sort(a):
    n = len(a)
    for j in range(1, n):
        key = a[j] # Cache Key
        i = j - 1
        while i >= 0 and a[i] > key: # Traverse back and find apt position and keep shifting
            a[i+1] = a[i]
            i -= 1
        a[i+1] = key # Insert current key into found position
    
a = [5, 2, 4, 6, 1, 3]
print a
sort(a)
print a
