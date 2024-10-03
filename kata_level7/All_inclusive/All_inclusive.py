def contain_all_rots(strng, arr):
    if strng == "":
        return True

    rotations = [strng[i:] + strng[:i] for i in range(len(strng))]

    return all(rotation in arr for rotation in rotations)