import string


def rot13(message):
    alpha = string.ascii_lowercase + string.ascii_lowercase
    big_alpha = string.ascii_uppercase + string.ascii_uppercase
    list_a = list(message)
    results = []
    for i in list_a:
        if i.islower():
            if i in alpha:
                results.append(alpha[alpha.index(i)+13])
            else:
                results.append(i)
        else:
            if i in big_alpha:
                results.append(big_alpha[big_alpha.index(i)+13])
            else:
                results.append(i)
        
    return "".join(results)
