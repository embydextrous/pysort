import math

def insertionSort(a):
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key

def bucketSort(a):
    n = len(a)
    numBuckets = int(math.sqrt(n))
    mini, maxi = min(a), max(a)
    step = (maxi - mini) / numBuckets if (maxi - mini) % numBuckets == 0 else (maxi - mini) / numBuckets + 1
    buckets = [[] for i in range(numBuckets)] # O(n)
    for i in a:
        buckets[(i - mini + 1) / step].append(i) # O(n)
    for bucket in buckets:
        insertionSort(bucket) # O(n) if elements are uniformly distributed.
    k = 0
    for bucket in buckets: # O(n)
        for i in bucket:
            a[k] = i
            k += 1


a = [24, 30, 32, 25, 28, 33, 24, 31, 27, 29, 30, 35, 34, 31, 24, 26, 28, 32, 35, 31, 24, 30, 33, 31, 26]
s = sorted(a)
bucketSort(a)
print a