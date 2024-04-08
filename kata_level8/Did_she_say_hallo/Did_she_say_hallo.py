def validate_hello(greetings):
    a = ["hello", 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']
    return any(word in greetings.lower() for word in a)
