import commands2
from subsystems.driveSubsystem import DriveSubsystem

class HalveDriveSpeed(commands2.Command):
    def __init__(self, drive: DriveSubsystem):
        super().__init__()

        self.drive = drive

    def initialize(self):
        self.drive.setMaxOutput(0.45)

    def end(self, interrupted: bool):
        self.drive.setMaxOutput(0.9)
       
    