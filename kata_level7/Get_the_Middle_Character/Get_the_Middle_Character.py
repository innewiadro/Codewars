def get_middle(s):
    mid = len(s) // 2 
    return s[mid - 1:mid + 1] if len(s) % 2 == 0 else s[mid:mid + 1]
