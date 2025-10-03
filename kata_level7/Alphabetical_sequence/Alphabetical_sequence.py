def alpha_seq(strng):
    return ",".join(sorted((ch.upper() + ch.lower() * (ord(ch.lower()) - ord('a'))) for ch in strng))
