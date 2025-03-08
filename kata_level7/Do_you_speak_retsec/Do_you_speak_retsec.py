def reverse_by_center(s):
    mid = len(s) //2
    if len(s) % 2:
        return s[mid+1:] +s[mid] + s[0:mid]
    else:
        return s[mid:] + s[0:mid]
