def count_languages(lst):
    result = {}

    for dev in lst:
        lang = dev['language']
        result[lang] = result.get(lang, 0) + 1

    return result