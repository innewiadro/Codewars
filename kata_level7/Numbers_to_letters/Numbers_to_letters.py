def switcher(arr):
    zyx = "zyxwvutsrqponmlkjihgfedcba!? "
    return "".join([zyx[int(i)-1] for i in arr])
