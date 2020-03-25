def bsearch(a, n, value):
    low = 0
    high = n - 1
    while low <= high:
        mid = low + (high - low) >> 1
        if a[mid] > value:
            high = mid - 1
        else:
            if mid == n - 1 or a[mid + 1] > value:
                return mid
            else:
                low = mid + 1
    return -1
