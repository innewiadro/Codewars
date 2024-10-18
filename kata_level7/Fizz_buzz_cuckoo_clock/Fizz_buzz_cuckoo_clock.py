def fizz_buzz_cuckoo_clock(time):
    hour, minute = map(int, time.split(":"))

    hour_12 = hour % 12 or 12

    if minute == 0:
        return " ".join(["Cuckoo"] * hour_12)
    elif minute == 30:
        return "Cuckoo"

    result = []
    if minute % 3 == 0:
        result.append("Fizz")
    if minute % 5 == 0:
        result.append("Buzz")

    if not result:
        return "tick"

    return " ".join(result)
