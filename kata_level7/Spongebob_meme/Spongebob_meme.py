def sponge_meme(s):
    return ''.join(c.lower() if i % 2 else c.upper() for i, c in enumerate(s))
