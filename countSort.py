def sort(a):
    maxi = max(a)
    mini = min(a)
    n = maxi - mini + 1
    count = [0] * n
    for i in a:
        count[i - mini] += 1
    k = 0
    for i in range(n):
        key = mini + i
        for j in range(count[i]):
            a[k] = key
            k += 1


a = [12, 14, 13, 11, 12, 12, 14, 13, 15, 18, 17, 19, 19, 17, 12, 11, 14, 15]
sort(a)
print a

# Time Complexity is O(n)
# Space Complexity is O(n)
# Useful if data is in a given range like list of marks in class.