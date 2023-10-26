def calfibo(n: int) -> int:
    res = 0
    a, b = 0, 1
    while b <= n:
        res += b
        tmp = b
        b += a
        a = tmp
    return res
