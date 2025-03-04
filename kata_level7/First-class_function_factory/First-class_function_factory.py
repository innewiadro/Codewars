def factory(x):
    def multiplier(arr):
        return [i * x for i in arr]
    return multiplier
