def compare(s1, s2):
    if s1 == None or s2 == None:
        return True

    if len(s1) == 0 or len(s2) == 0:
        return True

    for i in s1:

        if isinstance(i, int):
            return False

    for j in s2:

        if isinstance(j, int):
            return False

    for i in s1.upper():

        if i not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            return True
