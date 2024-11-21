def is_monotone(heights):
    return all(heights[i] >= heights[i - 1] for i in range(1, len(heights)))
