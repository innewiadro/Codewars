def multiply_all(a):
    def multiplier(n):
        return [x * n for x in a]
    return multiplier
