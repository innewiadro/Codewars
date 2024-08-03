def freq_seq(s, sep):
    res = ""
    for i in s:
        res += f'{s.count(i)}' + sep

    return res[:-1]
