from subsystems.driveSubsystem import DriveSubsystem
import commands2
from wpilib.shuffleboard import Shuffleboard
import constants

class Boost(commands2.command.Command):
    def __init__(self, drive: DriveSubsystem):
        self.drive = drive
        self.widget = Shuffleboard.getTab("State").add("Boost", False).withSize(10, 5).getEntry()


    def initialize(self):
        self.widget.setBoolean(True)
        self.drive.setMaxOutput(constants.kBoostSpeed)

    def end(self, interrupted: bool):
        self.widget.setBoolean(False)
        self.drive.setMaxOutput(constants.kRegSpeed)