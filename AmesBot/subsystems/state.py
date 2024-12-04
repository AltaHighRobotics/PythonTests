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
        if button == "Forward" and pressed: # Run score subsytems to accomplish objective
            print("Button FWD")
            if self.objective == "B": # Extend bucket
                if self.endstop != 1: # As long as the button hasn't hit the endstop, we can extend it
                    self.bucket == 1
                else:
                    self.bucket == 0 # Don't move the bucket it we're at the stop
            
            else: # Intake/Plow
                self.intake = 1 # Tell State we want to intake (if the bucket needs to RTH, the endstops will trigger
                #                  actual intaking when the bucket is back)

                if self.endstop == -1: # We can only intake if the bucket is all the way back
                    self.bucket == 0 # Stop the bucket
                    self.intaking = 1 # Actually run the intake
        
        elif button == "Back" and pressed: # Run score subsystems to accomplish objective
            print("Button BACK")
            if self.objective == "B": # Retract Bucket
                if self.endstop != -1: # Bottom endstop
                    self.bucket == -1
                else:
                    self.bucket == 0
            
            else: # Intake/Plow
                self.intake = -1
                self.intaking = -1 # Run the intake backwards (useful if the bot jams)
        
        

        elif button == 'Drive Mode' and pressed: # Change the drive mode
            print("Button DM")
            if self.driveMode == "FO":
                self.driveMode = "RO"
                self.updateDriveSide() # Since the robot can run on multiple sides in RO, set the side
            elif self.driveMode == "RO":
                self.driveMode = "FO" # FO is headless so we don't need to set the drive side   
        
        self.updateWidgets() # Update Shuffleboard to match the new state(s)