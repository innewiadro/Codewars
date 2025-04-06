def transpose(song, interval):
    sharp_notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

    flat_to_sharp = {
        'Bb': 'A#',
        'Db': 'C#',
        'Eb': 'D#',
        'Gb': 'F#',
        'Ab': 'G#'
    }

    normalized_song = [
        flat_to_sharp.get(note, note) for note in song
    ]

    transposed = []
    for note in normalized_song:
        index = sharp_notes.index(note)
        new_index = (index + interval) % 12
        transposed.append(sharp_notes[new_index])

    return transposed
