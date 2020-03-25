def bsearch(a, low, high, value):
    if low > high: return -1

    mid = low + (high - low) >> 1
    if a[mid] == value:
        return mid
    elif a[mid] < value:
        low = mid + 1
        return bsearch(a, low, high, value)
    else:
        high = mid - 1
        return bsearch(a, low, high, value)
