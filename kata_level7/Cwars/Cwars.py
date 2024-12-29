def initials(name):
    parts = name.split()
    initials = ".".join(part[0].upper() for part in parts[:-1])
    return f"{initials}.{parts[-1].capitalize()}"
