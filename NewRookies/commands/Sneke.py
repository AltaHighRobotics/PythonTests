from subsytems.driverSubsystem import DriveSubsystems
import commands2
import time

SLITHER_SPEED = 0.5
ROTATION_AMOUNT = 30 #Degrees

class Dance(commands2.command.Command):
    def __init__(self, drive: DriveSubsystems):
        self.drive = drive
        self.addRequirements(self.drive)

    def initialize(self):
        self.startTime = time.time()
    
    def execute(self) -> None:
        if time.time() - self.startTime >= 1:
            self.startTime = time.time()
        elif time.time() - self.startTime >= 0.5:
            self.drive.arcadeDrive(SLITHER_SPEED, ROTATION_AMOUNT)
        else:
            self.drive.arcadeDrive(SLITHER_SPEED, -ROTATION_AMOUNT)
        