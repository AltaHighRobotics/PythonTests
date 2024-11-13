from commands2 import Subsystem
import constants

import wpimath.geometry
import wpimath.kinematics
from subsystems.swerveModule import SwerveModule
import navx

class SwerveDrive(Subsystem):
    """
    Represents a swerve drive style drivetrain.
    """

    def __init__(self) -> None:
        super().__init__()

        self.frontLeftLocation = wpimath.geometry.Translation2d(constants.kSwerveModCtrToCtr/2, constants.kSwerveModCtrToCtr/2)
        self.frontRightLocation = wpimath.geometry.Translation2d(constants.kSwerveModCtrToCtr/2, -constants.kSwerveModCtrToCtr/2)
        self.backLeftLocation = wpimath.geometry.Translation2d(-constants.kSwerveModCtrToCtr/2, constants.kSwerveModCtrToCtr/2)
        self.backRightLocation = wpimath.geometry.Translation2d(-constants.kSwerveModCtrToCtr/2, -constants.kSwerveModCtrToCtr/2)

        self.frontLeft = SwerveModule(constants.kFLDriveID, constants.kFLTurnID, constants.kTurnFLP, constants.kTurnFLI, constants.kTurnFLD, constants.kTurnFLS, constants.kTrunFLV)
        self.frontRight = SwerveModule(constants.kFRDriveID, constants.kFRTurnID, constants.kTurnFRP, constants.kTurnFRI, constants.kTurnFRD, constants.kTurnFRS, constants.kTrunFRV)
        self.backLeft = SwerveModule(constants.kBLDriveID, constants.kBLTurnID, constants.kTurnBLP, constants.kTurnBLI, constants.kTurnBLD, constants.kTurnBLS, constants.kTrunBLV)
        self.backRight = SwerveModule(constants.kBRDriveID, constants.kBRTurnID, constants.kTurnBRP, constants.kTurnBRI, constants.kTurnBRD, constants.kTurnBRS, constants.kTrunBRV)
        
        self.maxOut = .75

        self.gyro = navx.AHRS.create_spi() # NavX

        self.driveSide = "F"

        self.kinematics = wpimath.kinematics.SwerveDrive4Kinematics(
            self.frontLeftLocation,
            self.frontRightLocation,
            self.backLeftLocation,
            self.backRightLocation,
        )

        self.gyro.reset()

    def drive(
        self,
        xSpeed: float,
        ySpeed: float,
        rot: float,
        fieldRelative: bool
    ) -> None:
        """
        Method to drive the robot using joystick info.
        :param xSpeed: Speed of the robot in the x direction (forward).
        :param ySpeed: Speed of the robot in the y direction (sideways).
        :param rot: Angular rate of the robot.
        :param fieldRelative: Whether the provided x and y speeds are relative to the field.
        """

        # Change the speeds so the robot moves relative to a side in robot oriented
        if not fieldRelative:
            if self.driveSide == "R":
                xSpeed, ySpeed = ySpeed, -xSpeed
            
            elif self.driveSide == "L":
                xSpeed, ySpeed = -ySpeed, xSpeed                                                

        swerveModuleStates = self.kinematics.toSwerveModuleStates(
            wpimath.kinematics.ChassisSpeeds.discretize(
                (
                    wpimath.kinematics.ChassisSpeeds.fromFieldRelativeSpeeds(
                        xSpeed, ySpeed, rot, -self.gyro.getRotation2d()
                    )
                    if fieldRelative
                    else wpimath.kinematics.ChassisSpeeds(xSpeed, ySpeed, rot)
                ),
                0.02
            )
        )
        wpimath.kinematics.SwerveDrive4Kinematics.desaturateWheelSpeeds(
            swerveModuleStates, self.maxOut/0.082 # 1/0.082 gives a maximum output of 1 for the drive controller's set() function
        )
        self.frontLeft.setDesiredState(swerveModuleStates[0])
        self.frontRight.setDesiredState(swerveModuleStates[1])
        #self.backLeft.setDesiredState(swerveModuleStates[2])
        #self.backRight.setDesiredState(swerveModuleStates[3])

    def setMaxOutput(self, maxOutput):
        self.maxOut = maxOutput