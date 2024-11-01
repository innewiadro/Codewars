def caffeine_buzz(n):
    result = ""

    if n % 3 == 0:
        result = "Java"
        if n % 4 == 0:
            result = "Coffee"
        if n % 2 == 0:
            result += "Script"

    if result == "":
        return "mocha_missing!"
    else:
        return result
