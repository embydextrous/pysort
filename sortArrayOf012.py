# Count Sort Based Method
def sort(a):
    count = [0] * 3
    for i in a:
        count[i] += 1
    k = 0
    for i in range(3):
        for j in range(count[i]):
            a[k] = i
            k += 1

# Dutch National Flag Algorithm
def sortDNF(a):
    l = m = 0
    r = len(a) - 1
    while m <= r:
        if a[m] == 0:
            a[l], a[m] = a[m], a[l]
            l += 1
            m += 1
        elif a[m] == 1:
            m += 1
        else:
            a[m], a[r] = a[r], a[m]
            r -= 1

a = [1, 2, 0, 2, 0, 2, 1, 0, 1, 2, 0, 2, 1, 2, 2, 1, 0]
sort(a)
print a
a = [1, 2, 0, 2, 0, 2, 1, 0, 1, 2, 0, 2, 1, 2, 2, 1, 0]
sortDNF(a)
print a
a = [1, 1, 1]
sortDNF(a)
print a