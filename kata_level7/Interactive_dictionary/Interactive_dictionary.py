class Dictionary():
    def __init__(self):
        self.entries = {}

    def newentry(self, word, definition):
        self.entries[word] = definition

    def look(self, word):
        return self.entries.get(word, f"Can't find entry for {word}")
