def rev_rot(strng, sz):
    if sz <= 0 or len(strng) < sz:
        return ""

    new_list = []

    for i in range(len(strng)):
        if i % sz == 0:
            chunk = strng[0 + i:sz + i]

            if len(chunk) == sz:
                if sum([int(i) for i in chunk]) % 2 == 0:
                    new_list.append(chunk[::-1])
                else:
                    new_list.append(chunk[1:] + chunk[0])
    return ''.join(new_list)
