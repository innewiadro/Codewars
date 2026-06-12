def sum_of_a_beach(beach):
    beach = beach.lower()
    words = ["water", "sand", "fish", "sun"]
    i = 0
    count = 0

    while i < len(beach):
        matched = False

        for w in words:
            if beach[i:i+len(w)] == w:
                count += 1
                i += len(w)
                matched = True
                break

        if not matched:
            i += 1

    return count
