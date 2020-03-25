def bsearch(a: list, n, value):
    low = 0
    high = n - 1
    while low <= high:
        mid = low + (high - low) >> 1
        if a[mid] > a[value]:
            high = mid - 1
        elif a[mid] < value:
            low = mid + 1
        else:
            if mid == 0 or a[mid - 1] != a[mid]:
                return mid
            else:
                high = mid - 1
    return -1
