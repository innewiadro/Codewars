def i_speak_french(sentence):
    sentences = sentence.split(".")
    result = []

    for s in sentences:
        s = s.strip()
        if not s:
            continue

        words = s.split()

        translated = []
        for i in range(len(words)):
            if i == 0:
                translated.append("Baguette")
            else:
                translated.append("baguette")

        translated.append("Encore!")
        result.append(" ".join(translated))

    return " ".join(result)
