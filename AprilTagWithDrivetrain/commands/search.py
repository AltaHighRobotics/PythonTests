from commands2 import Command

from subsystems.aprilTagSubsystem import AprilTagSubsystem

class Search(Command):
    def __init__(self, vision: AprilTagSubsystem):
        super().__init__()

        self.vision = vision
    
    def execute(self):
        self.vision.refresh()