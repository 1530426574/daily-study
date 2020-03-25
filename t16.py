def f(n, d={}):
    if n == 1:
        return 1
    if n == 2:
        return 2
    # 如果有就直接从字典中返回，没有就直接计算
    if d.get(n) is not None:
        return d.get(n)
    ret = f(n - 1) + f(n - 2)
    d[n] = ret
    return ret
