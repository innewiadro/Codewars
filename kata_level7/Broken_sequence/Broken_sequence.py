def find_missing_number(s):
    elements = s.split()

    if not elements or len(elements) == 0:
        return 0

    nums = []

    for e in elements:
        if not e.isdigit():
            return 1
        nums.append(int(e))
    nums.sort()

    for i in range(1, max(nums) + 1):
        if i not in nums:
            return i

    return 0
