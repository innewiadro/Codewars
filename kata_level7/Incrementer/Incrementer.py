def incrementer(nums):
    couter = 1
    new_nums = []
    for i in nums:
        number = i + couter
        couter += 1
        if number > 9:
            new_nums.append(int(str(number)[-1]))
        else:
            new_nums.append(number)

    return new_nums
