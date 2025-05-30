def what_note(string, fret):
    scale = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
    open_notes = {
        "E": "E",
        "A": "A",
        "D": "D",
        "G": "G",
        "B": "B",
        "e": "E"
    }
    open_note = open_notes[string]
    start_index = scale.index(open_note)
    note_index = (start_index + fret) % 12
    return scale[note_index]
