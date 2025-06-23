def heavy_metal_umlauts(text):
    umlaut_map = {
        'A': 'Ä', 'E': 'Ë', 'I': 'Ï', 'O': 'Ö', 'U': 'Ü', 'Y': 'Ÿ',
        'a': 'ä', 'e': 'ë', 'i': 'ï', 'o': 'ö', 'u': 'ü', 'y': 'ÿ',
    }
    return ''.join(umlaut_map.get(char, char) for char in text)
