class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.listeners = set()  # Store unique listeners

    def how_many(self, people):
        unique_new_listeners = {person.lower() for person in people}  # Convert names to lowercase
        new_listeners = unique_new_listeners - self.listeners  # Find new listeners
        self.listeners.update(new_listeners)  # Update the set with new listeners
        return len(new_listeners)
