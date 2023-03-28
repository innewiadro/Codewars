def number(lines):
    if lines == []:
        return lines
    for i in range(len(lines)):
        lines[i] = str(i+1) + ": " + lines[i]
    return lines
