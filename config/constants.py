

notes = ["C", "C#", "Db", "D", "D#", "Eb", "E", "F", "F#", "Gb", "G", "G#", "Ab", "A", "A#", "Bb", "B"]
scaleTypes = ["Major", "minor"]

majorScales = {
    "C": ["C", "D", "E", "F", "G", "A", "B", "C"],
    "C#": ["C#", "D#", "E#", "F#", "G#", "A#", "B#", "C#"],
    "Db": ["Db", "Eb", "F", "Gb", "Ab", "Bb", "C", "Db"],
    "D": ["D", "E", "F#", "G", "A", "B", "C#", "D"],
    "D#": ["D#", "E#", "F##", "G#", "A#", "B#", "C##", "D#"],
    "Eb": ["Eb", "F", "G", "Ab", "Bb", "C", "D", "Eb"],
    "E": ["E", "F#", "G#", "A", "B", "C#", "D#", "E"],
    "F": ["F", "G", "A", "Bb", "C", "D", "E", "F"],
    "F#": ["F#", "G#", "A#", "B", "C#", "D#", "E#", "F#"],
    "Gb": ["Gb", "Ab", "Bb", "Cb", "Db", "Eb", "F", "Gb"],
    "G": ["G", "A", "B", "C", "D", "E", "F#", "G"],
    "G#": ["G#", "A#", "B#", "C#", "D#", "E#", "F##", "G#"],
    "Ab": ["Ab", "Bb", "C", "Db", "Eb", "F", "G", "Ab"],
    "A": ["A", "B", "C#", "D", "E", "F#", "G#", "A"],
    "A#": ["A#", "B#", "C##", "D#", "E#", "F##", "G##", "A#"],
    "Bb": ["Bb", "C", "D", "Eb", "F", "G", "A", "Bb"],
    "B": ["B", "C#", "D#", "E", "F#", "G#", "A#", "B"]
}
minorScales = {
    "C": ["C", "D", "Eb", "F", "G", "Ab", "Bb", "C"],
    "C#": ["C#", "D#", "E", "F#", "G#", "A", "B", "C#"],
    "Db": ["Db", "Eb", "Fb", "Gb", "Ab", "Bbb", "Cb", "Db"],
    "D": ["D", "E", "F", "G", "A", "Bb", "C", "D"],
    "D#": ["D#", "E", "F#", "G#", "A#", "B", "C#", "D#"],
    "Eb": ["Eb", "F", "Gb", "Ab", "Bb", "Cb", "Db", "Eb"],
    "E": ["E", "F#", "G", "A", "B", "C", "D", "E"],
    "F": ["F", "G", "Ab", "Bb", "C", "Db", "Eb", "F"],
    "F#": ["F#", "G#", "A", "B", "C#", "D", "E", "F#"],
    "Gb": ["Gb", "Ab", "Bbb", "Cb", "Db", "Ebb", "Fb", "Gb"],
    "G": ["G", "A", "Bb", "C", "D", "Eb", "F", "G"],
    "G#": ["G#", "A", "B", "C#", "D#", "E", "F#", "G#"],
    "Ab": ["Ab", "Bb", "Cb", "Db", "Eb", "Fb", "Gb", "Ab"],
    "A": ["A", "B", "C", "D", "E", "F", "G", "A"],
    "A#": ["A#", "B", "C#", "D#", "E#", "F#", "G#", "A#"],
    "Bb": ["Bb", "C", "Db", "Eb", "F", "Gb", "Ab", "Bb"],
    "B": ["B", "C#", "D", "E", "F#", "G", "A", "B"],
}

majorChordDegrees = ["I", "ii", "iii", "IV", "V", "vi", "vii°"]
majorChordDegreeNotes = {
    "I": [1, 3, 5],     # Major chord
    "ii": [2, 4, 6],    # Minor chord
    "iii": [3, 5, 7],   # Minor chord
    "IV": [4, 6, 8],    # Major chord
    "V": [5, 7, 9],     # Major chord
    "vi": [6, 8, 10],   # Minor chord
    "vii°": [7, 9, 11], # Diminished chord
}

minorChordDegrees = ["i", "ii°", "III", "iv", "v", "VI", "VII"]
minorChordDegreeNotes = {
    "i": [1, 3, 5],      # Minor chord
    "ii°": [2, 4, 6],    # Diminished chord
    "III": [3, 5, 7],    # Major chord
    "iv": [4, 6, 8],     # Minor chord
    "v": [5, 7, 9],      # Minor chord
    "VI": [6, 8, 10],    # Major chord
    "VII": [7, 9, 11],   # Major chord
}

inversions = ["Root Position", "First Inversion", "Second Inversion"]

noteMap = {
    "C": 0,
    "C#" : 1,
    "Db" : 1,
    "D" : 2,
    "D#" : 3,
    "Eb" : 3,
    "E" : 4,
    "F" : 5,
    "F#" : 6,
    "Gb" : 6,
    "G" : 7,
    "G#" : 8,
    "Ab" : 8,
    "A" : 9,
    "A#" : 10,
    "Bb" : 10,
    "B" : 11
}


# chordVariety = ["Major", "minor", "suspended", "diminished", "Dominant7", "Major7", "minor7"]
