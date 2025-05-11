def largest_sum(s):
    substrings = s.split('0')
    return max(sum(int(digit) for digit in substring) for substring in substrings)