def correct_polish_letters(st):
    pol = {"ą": "a",
           "ć": "c",
           "ę": "e",
           "ł": "l",
           "ń": "n",
           "ó": "o",
           "ś": "s",
           "ź": "z",
           "ż": "z"}

    return "".join([pol[i] if i in pol else i for i in st])
