def bseach(a: list, n: int, value: int) -> None:
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + (high - low) >> 1)
        if a[mid] == value:
            return mid
        elif a[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return -1
