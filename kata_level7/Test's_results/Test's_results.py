def test(marks):
    class_average = round(sum(marks) / len(marks), 3)

    categories = {"h": 0, "a": 0, "l": 0}
    for mark in marks:
        if mark in (9, 10):
            categories["h"] += 1
        elif mark in (7, 8):
            categories["a"] += 1
        elif 1 <= mark <= 6:
            categories["l"] += 1

    if categories["h"] > 0 and categories["a"] == 0 and categories["l"] == 0:
        return [class_average, categories, "They did well"]

    return [class_average, categories]
