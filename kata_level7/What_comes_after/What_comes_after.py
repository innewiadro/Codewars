def comes_after(string, letter):
    result = ""
    lower_letter = letter.lower()
    for i in range(len(string) - 1):
        if string[i].lower() == lower_letter and string[i+1].isalpha():
            result += string[i+1]
    return result
