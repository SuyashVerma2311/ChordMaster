import config.constants as constants
from Scale import Scale

class Verify:
    def __init__(self, referenceChord, inversionCheck = False):
        self.playedNotes = []
        self.setReferenceNotes(referenceChord)
        self.inversionCheck = inversionCheck
    
    def clearPlayedNotes(self):
        self.playedNotes = []

    def addToPlayedNotes(self, midiMessage):
        note = self.convertFromMidiMessage(midiMessage=midiMessage)
        if note != 0:
            self.playedNotes.append(note)
    
    def setReferenceNotes(self, referenceChord):
        self.referenceNotes = self.convertFromChord(referenceChord)
    
    def verify(self):
        if not self.inversionCheck:
            self.referenceNotes.sort()
            self.playedNotes = [note%12 for note in self.playedNotes]
            self.playedNotes.sort()
        else:
            self.playedNotes.sort()
            self.playedNotes = [note%12 for note in self.playedNotes]
        return [set(self.playedNotes).issubset(set(self.referenceNotes)),
                        self.referenceNotes == self.playedNotes]
    
    def convertFromMidiMessage(self, midiMessage):
        return midiMessage[0][1] if midiMessage[0][2] != 0 and midiMessage[0][2] != 127 else 0

    def convertFromChord(self, chord):
        return self.map(chord=chord)
    
    def map(self, chord):
        return [constants.noteMap[noteChar] for noteChar in chord]
    
    def printReferenceChord(self):
        print("##################################")
        print(f"\tReference Chord: {self.referenceNotes}")
        print("##################################")
    
    def printPlayedNotes(self):
        print("##################################")
        print(f"\tNotes Played: {self.playedNotes}")
        print("##################################")


