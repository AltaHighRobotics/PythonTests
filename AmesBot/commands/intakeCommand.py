import commands2

from subsystems.intakeSubsystem import IntakeSubsystem

class Intake(commands2.Command):
    def __init__(self , intake: IntakeSubsystem) -> None:
        super().__init__()
        self.intake = intake
             
    def initialize(self) -> None:
        self.intake.setSpeed(0.8)

    def end(self, interrupted: bool) -> None:
        self.intake.setSpeed(0)

class Outtake(commands2.Command):
    def __init__(self , intake: IntakeSubsystem) -> None:
        super().__init__()
        self.intake = intake
             
    def initialize(self) -> None:
        self.intake.setSpeed(-0.8)

    def end(self, interrupted: bool) -> None:
        self.intake.setSpeed(0)