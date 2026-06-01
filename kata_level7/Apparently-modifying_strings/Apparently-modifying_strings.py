def apparently(st):
    if not st:
        return ""

    words = st.split()
    result = []
    i = 0

    while i < len(words):
        word = words[i]
        result.append(word)

        if word in ("and", "but"):
            if i + 1 < len(words) and words[i + 1] == "apparently":
                pass
            else:
                result.append("apparently")

        i += 1

    return " ".join(result)