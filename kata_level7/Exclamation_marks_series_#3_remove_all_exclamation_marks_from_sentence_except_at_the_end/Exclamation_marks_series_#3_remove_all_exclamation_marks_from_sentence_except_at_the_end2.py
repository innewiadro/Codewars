def remove(s):
    stripped = s.rstrip("!")
    trailing = s[len(stripped):]
    return stripped.replace("!", "") + trailing
