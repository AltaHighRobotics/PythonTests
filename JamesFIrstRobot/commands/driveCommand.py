import typing
import commands2
from subsystems.driveSubsystem import DriveSubsystem

class DriveCommand(commands2.Command):
    def __init__(self, drive: DriveSubsystem, foreward: typing.Callable[[], float], rotation: typing.Callable[[], float]):
        super().__init__()

        self.drive = drive
        self.rotate = rotation
        self.foreward = foreward

        self.addRequirements(self.drive)

    def execute(self):
        self.drive.joystickDrive(self.foreward(), self.rotate() )


        
