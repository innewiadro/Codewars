def longest_palindrome (s):
    if not s:
        return 0

    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    max_length = 0

    for i in range(len(s)):
        len1 = expand(i, i)
        len2 = expand(i, i + 1)

        max_length = max(max_length, len1, len2)

    return max_length