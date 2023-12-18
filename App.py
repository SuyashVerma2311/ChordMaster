from Scale import Scale
from Timer import Timer
from AudioEngine import AudioEngine
from Verify import Verify
from Report import Report
from config import properties
from config import constants
from config.decorators import *
import keyboard
import os
import sys

class App:
    def __init__(self):
        self.scale = Scale(rootNote=properties.rootNote, scaleType=properties.scaleType, inversionCheck=properties.inversionCheck)
        self.verify = Verify(self.scale.chord, inversionCheck=properties.inversionCheck)
        self.timer = Timer(initialTimeLimit=properties.initialTimeLimit, decreasingTime=properties.decreasingTime, progressTimeFactor=properties.progressTimeFactor)
        self.responseTimes = []
        self.roundNumber = 0
        try:
            self.AudioEngine = AudioEngine()
        except Exception as e:
            print("!!!!!ERROR: Could not connect to a MIDI Device!")
            exit()
    
    def prepNewRound(self):
        os.system('cls')
        self.scale.generateRandomChord()
        self.verify.setReferenceNotes(referenceChord=self.scale.chord)
        self.verify.clearPlayedNotes()
        self.timer.resetTimer(roundNumber=self.roundNumber)
        self.scale.printChord()
        self.timer.displayTimer()
        self.AudioEngine.say(text=self.scale.chordName)
        if properties.referenceAudioPlayback:
            self.AudioEngine.playMidi(chord=self.verify.referenceNotes)

    def run(self):
        while True:                                                         # New Chord Loop (Game Progress Loop)
            self.prepNewRound()
            while True:                                                     # Listener Loop
                if keyboard.is_pressed('Esc'):
                    os.system('cls')
                    self.exit()
                midiMessage = self.AudioEngine.listenMidi()
                if midiMessage:    
                    self.verify.addToPlayedNotes(midiMessage=midiMessage)
                    correctNotes, completeChord = self.verify.verify()
                    if not correctNotes:                                    # Document this as wrong Note
                        self.wrongNote()
                    if completeChord:                                       # Document this as success + time taken
                        self.roundNumber += 1
                        break
                if self.timer.timesUp():
                    self.timesUp()                                          # Document this as timesUp
                self.timer.displayTimer()
                self.timer.sleep(0.01)
    
    def wrongNote(self):
        self.AudioEngine.say("WRONG CHORD!")
        os.system('cls')
        print("Wrong Chord Played!")
        self.gameOver()

    def timesUp(self):
        os.system('cls')
        print("Time's Up")
        self.gameOver()

    def exit(self):
        del self.AudioEngine
        sys.stdout.write(f'\033[?25h')
        sys.stdout.flush()
        exit()
   
    def gameOver(self):
        print("Exiting Now!")                                               # Generate Report here
        print("Keep Practicing!")
        self.exit()



if __name__ == "__main__":
    app = App()
    app.run()