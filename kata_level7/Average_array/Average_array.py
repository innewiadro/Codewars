def avg_array(arrs):
    return [sum(nums) / len(nums) for nums in zip(*arrs)]
