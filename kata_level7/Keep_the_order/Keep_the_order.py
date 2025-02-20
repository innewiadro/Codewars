import bisect


def keep_order(ary, val):
    return bisect.bisect_left(ary, val)
