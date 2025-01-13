def sort_vowels(s):
    if not isinstance(s, str):
        return ""

    vowels = "aeiouAEIOU"
    result = []

    for char in s:
        if char in vowels:
            result.append(f"|{char}")
        else:
            result.append(f"{char}|")

    return "\n".join(result)
