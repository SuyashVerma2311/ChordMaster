import config.constants as constants
import random

class Scale:
    def __init__(self, rootNote = None, scaleType = None, inversionCheck = False):
        self.inversionCheck = inversionCheck
        self.setRootNote(rootNote)
        self.setScaleType(scaleType)
        self.getScale()
        self.generateRandomChord()

    def setRootNote(self, rootNote):
        if rootNote is None:
            self.rootNote = random.choice(constants.notes)
        else:
            if rootNote in constants.notes:
                self.rootNote = rootNote
            else:
                print("Invalid Note!")
                exit()
    
    def setScaleType(self, scaleType):
        if scaleType is None:
            self.scaleType = random.choice(constants.scaleTypes)
        else:
            if scaleType in constants.scaleTypes:
                self.scaleType = scaleType
            else:
                print("Invalid Scale Type!")
                exit()
    
    def getScale(self):
        if self.scaleType == "Major":
            self.scale = constants.majorScales[self.rootNote]
        elif self.scaleType == "minor":
            self.scale = constants.minorScales[self.rootNote]
        else:
            print("Error Occurred! Cannot Get Scales for {self.rootNote} {self.chordType}")
    
    def generateRandomChord(self):
        if self.scaleType == "Major":
            self.chordDegree = random.choice(constants.majorChordDegrees)
            self.chord = [self.scale[(degreeNote - 1)%7] for degreeNote in constants.majorChordDegreeNotes[self.chordDegree]]
            self.chordName = self.scale[constants.majorChordDegrees.index(self.chordDegree)]
        elif self.scaleType == "minor":
            self.chordDegree = random.choice(constants.minorChordDegrees)
            self.chord = [self.scale[(degreeNote - 1)%7] for degreeNote in constants.minorChordDegreeNotes[self.chordDegree]]
            self.chordName = self.scale[constants.minorChordDegrees.index(self.chordDegree)]
        else:
            print("Invalid Scale Type!")
            exit()
        if self.chordDegree[-1] == '°':
            self.chordName += " Diminished"
        elif self.chordDegree[0] == 'i' or self.chordDegree[0] == 'v':
            self.chordName += " minor"
        elif self.chordDegree[0] == 'I' or self.chordDegree[0] == 'V':
            self.chordName += " Major"
        else:
            print("Invalid Chord Degree!")
            exit()
        self.setInversion()
    
    def setInversion(self):
        if self.inversionCheck:
            self.inversion = random.choice(constants.inversions)
        else:
            self.inversion = constants.inversions[0]
        if self.inversion[0] == "F":
            self.chord = [self.chord[1], self.chord[2], self.chord[0]]
        elif self.inversion[0] == "S":
            self.chord = [self.chord[2], self.chord[0], self.chord[1]]
            

    def printScale(self):
        print("##################################")
        print(f"\tScale: {self.rootNote} {self.scaleType}")
        print(f"\tScale: {self.scale}")
        print("##################################")

    def printChord(self):
        print("##################################")
        print(f"\tChord: {self.chordName} ({self.inversion})")
        print(f"\tChord: {self.chordDegree} Chord in {self.rootNote} {self.scaleType} Scale")
        print(f"\tChord: {self.chord}")
        print("##################################")