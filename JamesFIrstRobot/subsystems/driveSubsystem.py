import commands2
import wpilib
import wpilib.drive
import phoenix5 as ctre
 
import constants

class DriveSubsystem(commands2.Subsystem):
    def __init__(self):
        super().__init__()
        self.left1 = ctre.WPI_VictorSPX(constants.KLeftMotor1ID)
        self.left2 = ctre.WPI_VictorSPX(constants.KLeftMotor2ID)
        self.right1 = ctre.WPI_VictorSPX(constants.KRightMotor1ID)
        self.right2 = ctre.WPI_VictorSPX(constants.KRightMotor2ID)
        
        self.left1.setNeutralMode(ctre.NeutralMode.Brake)
        self.left2.setNeutralMode(ctre.NeutralMode.Brake)
        self.right1.setNeutralMode(ctre.NeutralMode.Brake)
        self.right2.setNeutralMode(ctre.NeutralMode.Brake)

        self.left = wpilib.MotorControllerGroup(self.left1, self.left2)
        self.right = wpilib.MotorControllerGroup(self.right1, self.right2)

        self.left.setInverted(True)

        self.drive = wpilib.drive.DifferentialDrive(self.left, self.right)

        self.drive.setMaxOutput(0.9)

    def joystickDrive(self, Forward: float, Rotation: float):

        self.drive.arcadeDrive(Forward, Rotation)
    
    def setMaxOutput(self, maxOutput: float):

        self.drive.setMaxOutput(maxOutput)
        
    



