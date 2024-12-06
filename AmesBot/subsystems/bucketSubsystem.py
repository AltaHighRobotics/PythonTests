from commands2 import Subsystem
import constants

class BucketSubsystem(Subsystem):

    def __init__(self) -> None:
        super().__init__()

    def setSpeed(self, speed: float):
        print(speed)