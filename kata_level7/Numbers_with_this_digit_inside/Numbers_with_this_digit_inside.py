def numbers_with_digit_inside(x, d):
    nums = [i for i in range(1, x + 1) if str(d) in str(i)]

    if not nums:
        return [0, 0, 0]

    product = 1
    for n in nums:
        product *= n

    return [len(nums), sum(nums), product]