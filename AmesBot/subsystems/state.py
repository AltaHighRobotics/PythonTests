from re import I, S
import commands2
import constants
from wpilib.shuffleboard import Shuffleboard
from subsystems.swerveDrive import SwerveDrive

class State(commands2.Subsystem):
    def __init__(self, drive: SwerveDrive):
        super().__init__()

        self.driveMode = constants.kDefaultDriveMode
        self.driveSide = constants.kDefaultDriveSide
        #self.halfSpeed = constants.kDefaultIsHalfSpeed
        self.objective = constants.kDefaultObjective
        self.bucket = constants.kDefaultBucket
        self.intake = constants.kDefaultIntake
        self.endstop = constants.kDefaultEndStop 
        self.intaking = self.intake       

        self.drive = drive

        # Each drive mode 'remembers' if it is in halfspeed or is inverted
        self.FOConfigs = (self.halfSpeed)
        self.ROConfigs = (self.driveSide, self.halfSpeed)

        # Shuffleboard widgets
        self.tab = Shuffleboard.getTab("State")
        self.driveModeWidget = self.tab.add("Drive Mode", "Default").getEntry()
        self.driveSidevWidget = self.tab.add("Drive Side", "Default").getEntry()
        self.objectiveWidget = self.tab.add("I", "Default").getEntry()

    def updateDriveSide(self):
        print("updating")
        self.drive.driveSide = self.driveSide

    def isDriveFO(self):
        #print(self.driveMode)
        return self.driveMode == "FO"
    
    #def isDriveHalfSpeed(self):
        #return self.halfSpeed != False

    def isExtending(self):
        return self.bucket == 1

    def isRetracting(self):
        return self.bucket == -1
    
    def isIntaking(self):
        return self.intaking == 1

    def isOutaking(self):
        return self.intaking == -1
    
    def updateWidgets(self):
        # Update the displayed state values
        print(self.driveSide)
        self.driveModeWidget.setString("Feild Oriented" if self.driveMode == "FO" else "Robot Oriented")
        self.driveSidevWidget.setString("N/A" if self.isDriveFO() else {"F": "Front", "R": "Right", "L": "Left"}[self.driveSide]) # Maps abbreviations to words
        self.objectiveWidget.setString({"I": "Intake", "P": "Plow", "B": "Bucket"}[self.driveSide])


    def handleButton(self, button, pressed):
        if button == "Forward" and pressed:
            print("Button FWD")
            if self.objective == "B":
                if self.endstop != 1:
                    self.bucket == 1
                else:
                    self.bucket == 0
            
            else:
                self.intake = 1
                if self.endstop == -1:
                    self.bucket == 0
                    self.intaking = 1
        
        if button == "Back" and pressed:
            print("Button BACK")
            if self.objective == "B":
                if self.endstop != -1:
                    self.bucket == -1
                else:
                    self.bucket == 0
            
            else:
                self.intake = -1
                self.intaking = -1
        
        

        if button == 'a' and pressed: # Change the drive mode
            print("Button A")
            if self.driveMode == "FO":
                self.driveMode = "RO"
                self.updateDriveSide()
            elif self.driveMode == "RO":
                self.driveMode = "FO"
        
        elif button == 'b' and pressed: # Toggle halfspeed
            print("Button B")
            self.halfSpeed = not self.halfSpeed        
        
        elif button == 'c' and pressed: # Cycle left thru drive sides (only works in robot oriented)
            print("Button C")
            if self.driveMode == "RO":
                self.driveSide = "F" if self.driveSide == "R" else "R" if self.driveSide == "L" else "L"
                self.updateDriveSide()

        elif button == 'd' and pressed: # Cycle right thru drive sides (only works in robot oriented)
            print("Button d")
            if self.driveMode == "RO":
                self.driveSide = "L" if self.driveSide == "R" else "R" if self.driveSide == "F" else "F"
                self.updateDriveSide()
        
        self.updateWidgets() # Update Shuffleboard to match the new state(s)