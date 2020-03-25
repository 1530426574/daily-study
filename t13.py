def bsearch(a, n, value):
    low = 0
    high = n - 1
    while low < high:
        mid = low + (high - low) >> 1
        if a[mid] < value:
            low = mid + 1
        elif a[mid] > value:
            high = mid - 1
        else:  # 相等并且是最后一个
            if mid == n - 1 or a[mid] != a[mid + 1]:
                return mid
            else:  # 虽然相等，但不是最后一个哦
                low = mid + 1
    return -1
