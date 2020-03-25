def f(n):
    if n == 1: return 1
    if n == 2: return 2
    pre = 1
    cur = 1
    ret = 0
    for i in range(3, n):
        ret = pre + cur
        pre, cur = cur, ret

    return ret


print(f(9))
