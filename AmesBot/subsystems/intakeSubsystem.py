from commands2 import Subsystem
import constants

class IntakeSubsystem(Subsystem):
    """
    Represents a swerve drive style drivetrain.
    """

    def __init__(self) -> None:
        super().__init__()

    def setSpeed(self, speed):
        print(speed)
        