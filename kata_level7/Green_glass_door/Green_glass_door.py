def step_through_with(s):
    return any(s[i] == s[i + 1] for i in range(len(s) - 1))