def status(nums):
    result = []
    for i, val in enumerate(nums):
        less_than = sum(1 for x in nums if x < val)
        stat = i + less_than
        result.append((stat, i, val))
    result.sort()
    return [val for _, _, val in result]
