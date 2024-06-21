def nickname_generator(name):
    if len(name) > 3:
        return name[:4] if name[2] in "aeoui" else name[:3]
    else:
        return "Error: Name too short"
