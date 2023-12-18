import time, sys
from config.decorators import *
from config import properties


class Timer:
    def __init__(self, initialTimeLimit, decreasingTime = False, progressTimeFactor = 1):
        self.timeLimit = initialTimeLimit
        self.initialTimeLimit = initialTimeLimit
        self.decreasingTime = decreasingTime
        self.progressTimeFactor = progressTimeFactor
        self.time = time
    
    def resetTimer(self, roundNumber=0):
        if self.decreasingTime:
            self.timeLimit = max(properties.minTimeLimit,self.initialTimeLimit * (self.progressTimeFactor ** roundNumber))
        else:
            self.timeLimit = self.initialTimeLimit
        self.initialTimeLimit = self.timeLimit
    
    def countdown(self, timeStep = 0.01):
        self.timeLimit = round(self.timeLimit - timeStep, 3)

    def sleep(self, timeStep = 0.01):
        self.countdown(timeStep=timeStep)
        self.time.sleep(0.01)
        pass
    
    def isInteger(self):
        return int(round(self.timeLimit,3)) == round(self.timeLimit,3)
    
    def timesUp(self):
        return round(self.timeLimit,3) <= 0

    def displayTimer(self):
        if self.isInteger():
            print(f"\tRemainingTime: {round(self.timeLimit)} seconds out of {round(self.initialTimeLimit)} seconds.")
            sys.stdout.write(f'\033[1A\033[?25l')
            sys.stdout.flush()

    def printTimer(self):
        print("##################################")
        print(f"\tRemainingTime: {round(self.timeLimit)} seconds out of {round(self.initialTimeLimit)} seconds.")
        print("##################################")