from commands2 import Subsystem
import constants

class IntakeSubsystem(Subsystem):
    """
    Represents a 2 motor flywheel intake system
    """

    def __init__(self) -> None:
        super().__init__()

    def setSpeed(self, speed): # Print out the speed so we know everything's woring TODO: actually move the motors
        print(speed)
        