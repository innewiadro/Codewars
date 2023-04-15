def printer_error(s):
    a = "abcdefghijklm"
    count = 0
    for i in s:
        if i not in a:
            count += 1
            
    return f"{count}/{len(s)}"
