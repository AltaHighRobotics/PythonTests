import commands2
import wpilib.shuffleboard
import constants
from wpilib.shuffleboard import Shuffleboard
from subsystems.swerveDrive import SwerveDrive
from wpilib import SmartDashboard
import wpilib

class State(commands2.Subsystem):
    def __init__(self, drive: SwerveDrive):
        super().__init__()

        # self.driveMode = constants.kDefaultDriveMode # "RO": robot oriented, "FO": feild oriented
        # self.driveSide = constants.kDefaultDriveSide # "F": front, "L": left, "R": right
        #self.halfSpeed = constants.kDefaultIsHalfSpeed
        self.objective = constants.kDefaultObjective # "P": plow, "I": intake, "B": bucket
        self.bucket = constants.kDefaultBucket # 1: moving out, 0: idle, -1: moving in
        self.intake = constants.kDefaultIntake # Desired state of intake (intake can't run if the bucket is out) 1: intaking, 0: idle, -1: outtake
        self.endstop = constants.kDefaultEndStop # 1: fully out, 0: middle, -1: fully in
        self.intaking = self.intake # 1: intaking, 0: idle, -1: outtake
        self.endstopOverride = constants.kDefaultEndStopOverride # User can overide the endstops if they are not working 0: not overridden, 1 overridden

        self.drive = drive # drivetrain

        # Shuffleboard widgets
        self.tab = Shuffleboard.getTab("State")
        # self.driveModeWidget = self.tab.add("Drive Mode", "Default").getEntry()
        # self.driveSidevWidget = self.tab.add("Drive Side", "Default").getEntry()
        self.objectiveWidget = self.tab.add("Objective", "Default").getEntry()
        self.endstopOverrideWidget = wpilib.SendableChooser()
        self.endstopOverrideWidget.setDefaultOption("OFF", False)
        self.endstopOverrideWidget.addOption("ON", True)
        self.tab.add("Endstop Override", self.endstopOverrideWidget)
    #def updateDriveSide(self):
       # print("updating")
        #self.drive.driveSide = self.driveSide

    #def isDriveFO(self):
        #print(self.driveMode)
        #return self.driveMode == "FO"
    
    #def isDriveHalfSpeed(self):
        #return self.halfSpeed != False

    def isEndstopOverride(self):
        self.endstopOverride = self.endstopOverrideWidget.getSelected()
        return self.endstopOverride
    
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
        #print(self.driveSide)
        #self.driveModeWidget.setString("Feild Oriented" if self.driveMode == "FO" else "Robot Oriented")
        #self.driveSidevWidget.setString("N/A" if self.isDriveFO() else {"F": "Front", "R": "Right", "L": "Left"}[self.driveSide]) # Maps abbreviations to words
        self.objectiveWidget.setString({"I": "Intake", "P": "Plow", "B": "Bucket"}[self.objective])


    def handleButton(self, button, pressed):
        if button == "Forward": # Run score subsytems to accomplish objective
            if pressed:
                print("Button FWD")
                if self.objective == "B": # Extend bucket
                    if self.endstop != 1 or self.endstopOverride: # As long as the button hasn't hit the endstop, we can extend it
                        self.bucket = 1
                    else:
                        self.bucket = 0 # Don't move the bucket it we're at the stop
                
                else: # Intake/Plow
                    self.intake = 1 # Tell State we want to intake (if the bucket needs to RTH, the endstops will trigger
                    #                  actual intaking when the bucket is back)
                    self.bucket = -1

                    if self.endstop == -1 or self.endstopOverride: # We can only intake if the bucket is all the way back
                        self.bucket = 0 # Stop the bucket
                        self.intaking = 1 # Actually run the intake
                    
            else:
                self.bucket = 0
                self.intake = 0
                self.intaking = 0

        elif button  == "Bucket" and pressed:
            self.objective = "B"

        elif button == "Plow" and pressed:
            self.objective = "P"

        elif button == "Intake" and pressed:
            self.objective = "I"

        elif button == "Back": # Run score subsystems to accomplish objective
            if pressed:
                print("Button BACK")
                if self.objective == "B": # Retract Bucket
                 if self.endstop != -1 or self.endstopOverride: # Bottom endstop
                    self.bucket = -1
                 else:
                    self.bucket = 0
            
                else: # Intake/Plow
                 self.intake = -1
                 self.intaking = -1 # Run the intake backwards (useful if the bot jams)
            else:
                self.bucket = 0
                self.intake = 0
                self.intaking = 0
        
        

        #elif button == 'Drive Mode' and pressed: # Change the drive mode
            #print("Button DM")
            #if self.driveMode == "FO":
               # self.driveMode = "RO"
                #self.updateDriveSide() # Since the robot can run on multiple sides in RO, set the side
            #elif self.driveMode == "RO":
                #self.driveMode = "FO" # FO is headless so we don't need to set the drive side   
        
        elif button == "Out" and not self.endstopOverride:
            if pressed:
                self.bucket = 0 # Stop the bucket
                self.endstop = 1 # Tell State the bucket is fully out

            else:
                self.endstop = 0 # Tell State we're somewhere in the middle

        elif button =="In" and not self.endstopOverride:
            if pressed:
                self.bucket = 0 # Stop the bucket
                self.endstop = -1 # Tell State that the bucket is fully in
                if self.intake == 1:
                    self.intaking = 1
            
            else:
                self.endstop = 0 # Tell State we're somewhere in the middle
                

        self.updateWidgets() # Update Shuffleboard to match the new state(s)