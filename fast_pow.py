def fast_pow(b, e):
    if e == 0:
        return 1

    tmp = fast_pow(b, e // 2)
    result = tmp * tmp

    if e % 2 == 1:
        result *= b

    return result


def fasat_pow2(b, e):
    res = 1

    while e > 0:
        if e % 2 == 1:
            res *= b

        b *= b
        e /= 2

    return res
