def ensure_question(s):
    if s.endswith("?"):
        return s
    else:
        return s + "?"
