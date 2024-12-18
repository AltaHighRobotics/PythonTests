from subsystems.driveSubsystem import DriveSubsystem
import commands2

class Boost(commands2.command.Command):
    def __init__(self, drive: DriveSubsystem):
        self.drive = drive

    def initialize(self):
        print("boost ON")
        self.drive.setMaxOutput(.95)

    def end(self, interrupted: bool):
        print("boost OFF")
        self.drive.setMaxOutput(.5)