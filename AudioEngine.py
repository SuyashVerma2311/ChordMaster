import rtmidi
import pyttsx3
import time

class AudioEngine:
    def __init__(self):
        self.midiIn = rtmidi.MidiIn()
        self.midiIn.open_port(0)
        self.midiOut = rtmidi.MidiOut()
        if self.midiOut.get_ports(): 
            self.midiOut.open_port(0)
        else:
            self.midiOut.open_virtual_port("Virtual MIDI Port")
        self.ttsEngine = pyttsx3.init()
    
    def listenMidi(self):
        return self.midiIn.get_message()
    
    def playMidi(self, chord):
        for note in chord:
            self.midiOut.send_message([144, note + 60, 100])
        time.sleep(0.5)
        for note in chord:
            self.midiOut.send_message([144, note + 60, 0])
        time.sleep(0.01)

    def say(self, text):
        self.ttsEngine.say(text=text)
        self.ttsEngine.runAndWait()
