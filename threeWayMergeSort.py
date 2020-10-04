def mergeSort(a):
    n = len(a)
    if len(a) > 2:
        d = n / 3
        q = n % 3
        left = a[:d + q]
        mid = a[d + q: 2 * d + q]
        right = a[2 * d + q:]
        mergeSort(left)
        mergeSort(mid)
        mergeSort(right)
        merge(a, left, mid, right)
    elif n == 2:
        if a[0] > a[1]:
            a[1], a[0] = a[0], a[1]


def merge(a, left, mid, right):
    i = j = k = z = 0

    while i < len(left) and j < len(mid) and k < len(right):
        a[z] = min(left[i], mid[j], right[k])
        if a[z] == left[i]:
            i += 1
        elif a[z] == mid[j]:
            j += 1
        else:
            k += 1
        z += 1

    while i < len(left) and j < len(mid):
        a[z] = min(left[i], mid[j])
        if a[z] == left[i]:
            i += 1
        else:
            j += 1
        z += 1

    while i < len(left) and k < len(right):
        a[z] = min(left[i], right[k])
        if a[z] == left[i]:
            i += 1
        else:
            k += 1
        z += 1

    while k < len(right) and j < len(mid):
        a[z] = min(right[k], mid[j])
        if a[z] == right[k]:
            k += 1
        else:
            j += 1
        z += 1

    while i < len(left):
        a[z] = left[i]
        i += 1
        z += 1

    while j < len(mid):
        a[z] = mid[j]
        j += 1
        z += 1

    while k < len(right):
        a[z] = right[k]
        k += 1
        z += 1

a = [9, 4, 11, 19, 1, 17, 6, 8, 20, 15, 2, 7, 18, 12, 5, 16, 13, 14, 10, 3]
mergeSort(a)
print a
