def explode(arr):
    nums = [n for n in arr if isinstance(n, (int, float))]
    if not nums:
        return "Void!"
    score = sum(nums)
    return [arr] * score
