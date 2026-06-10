def tiy_fizz_buzz(string):
    vowels = "aeiouAEIOU"
    result = ""

    for ch in string:
        if ch.isalpha():
            if ch in "AEIOU":
                result += "Iron Yard"
            elif ch in "aeiou":
                result += "Yard"
            elif ch.isupper():
                result += "Iron"
            else:
                result += ch
        else:
            result += ch

    return result
