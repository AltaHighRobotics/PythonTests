import commands2
import constants
from wpilib.shuffleboard import Shuffleboard

class State(commands2.Subsystem):
    def __init__(self):
        super().__init__()

        self.driveMode = constants.kDefaultDriveMode
        self.driveSide = constants.kDefaultDriveSide
        self.halfSpeed = constants.kDefaultIsHalfSpeed

        # Each drive mode 'remembers' if it is in halfspeed or is inverted
        self.FOConfigs = (self.halfSpeed)
        self.ROConfigs = (self.driveSide, self.halfSpeed)

        # Shuffleboard widgets
        self.tab = Shuffleboard.getTab("State")
        self.driveModeWidget = self.tab.add("Drive Mode", "Default").getEntry()
        self.driveSidevWidget = self.tab.add("Drive Side", "Default").getEntry()
        self.driveSpeedWidget = self.tab.add("Drive Speed", "Default").getEntry()

    def isDriveFO(self):
        #print(self.driveMode)
        return self.driveMode == "FO"
    
    def isDriveSideL(self):
        return self.driveSide == 'L'
    
    def isDriveSideF(self):
        return self.driveSide == 'F'
    
    def isDriveSideR(self):
        return self.driveSide == 'R'
    
    def isDriveHalfSpeed(self):
        return self.halfSpeed != False
    
    def updateWidgets(self):
        # Update the displayed state values
        print(self.driveSide)
        self.driveModeWidget.setString("Feild Oriented" if self.driveMode == "FO" else "Robot Oriented")
        self.driveSidevWidget.setString("N/A" if self.isDriveFO() else {"F": "Front", "R": "Right", "L": "Left"}[self.driveSide]) # Maps abbreviations to words
        self.driveSpeedWidget.setString("1/2" if self.halfSpeed else "3/4")


    def handleButton(self, button, pressed):
        if button == 'a' and pressed: # Change the drive mode
            print("Button A")
            if self.driveMode == "FO":
                self.FOConfigs = self.halfSpeed
                self.driveSide, self.halfSpeed = self.ROConfigs
                self.driveMode = "RO"
            elif self.driveMode == "RO":
                self.ROConfigs = (self.driveSide, self.halfSpeed)
                self.halfSpeed = self.FOConfigs
                self.driveMode = "FO"
        
        elif button == 'b' and pressed: # Toggle halfspeed
            print("Button B")
            self.halfSpeed = not self.halfSpeed        
        
        elif button == 'c' and pressed: # Cycle left thru drive sides (only works in robot oriented)
            print("Button C")
            if self.driveMode == "RO":
                self.driveSide = "F" if self.driveSide == "R" else "R" if self.driveSide == "L" else "L"

        elif button == 'd' and pressed: # Cycle right thru drive sides (only works in robot oriented)
            print("Button d")
            if self.driveMode == "RO":
                self.driveSide = "L" if self.driveSide == "R" else "R" if self.driveSide == "F" else "F"
        
        self.updateWidgets() # Update Shuffleboard to match the new state(s)