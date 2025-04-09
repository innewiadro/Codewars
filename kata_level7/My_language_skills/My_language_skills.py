def my_languages(results):
    return [language for language, score in sorted(results.items(), key=lambda x: x[1], reverse=True) if score >= 60]
