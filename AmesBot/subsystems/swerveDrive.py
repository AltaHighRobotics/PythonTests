from commands2 import Subsystem
import constants

import wpimath.geometry
import wpimath.kinematics
from subsystems.swerveModule import SwerveModule
import navx
import ntcore

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

        self.frontLeft = SwerveModule(constants.kFLDriveID, constants.kFLTurnID,
                                      constants.kTurnFLP, constants.kTurnFLI, constants.kTurnFLD)
        self.frontRight = SwerveModule(constants.kFRDriveID, constants.kFRTurnID,
                                       constants.kTurnFRP, constants.kTurnFRI, constants.kTurnFRD)
        self.backLeft = SwerveModule(constants.kBLDriveID, constants.kBLTurnID,
                                     constants.kTurnBLP, constants.kTurnBLI, constants.kTurnBLD)
        self.backRight = SwerveModule(constants.kBRDriveID, constants.kBRTurnID,
                                      constants.kTurnBRP, constants.kTurnBRI, constants.kTurnBRD)
        
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
        nt = ntcore.NetworkTableInstance.getDefault()

        # Start publishing an array of module states with the "/SwerveStates" key
        topic = nt.getStructArrayTopic("/SwerveStates", wpimath.kinematics.SwerveModuleState)
        self.pub = topic.publish()

    def drive(
        self,
        ySpeed: float,
        xSpeed: float,
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
            wpimath.kinematics.ChassisSpeeds.fromFieldRelativeSpeeds(
                -xSpeed, -ySpeed, rot, -self.gyro.getRotation2d()
            )
            if fieldRelative
            else wpimath.kinematics.ChassisSpeeds(-xSpeed, -ySpeed, rot)
        )

        self.pub.set([swerveModuleStates[0],swerveModuleStates[1],swerveModuleStates[2],swerveModuleStates[3]])
        #self.pub.set([wpimath.kinematics.SwerveModuleState.optimize(swerveModuleStates[0], self.frontLeft.getEncoder()),wpimath.kinematics.SwerveModuleState.optimize(swerveModuleStates[1], self.frontRight.getEncoder()),wpimath.kinematics.SwerveModuleState.optimize(swerveModuleStates[2], self.backLeft.getEncoder()),wpimath.kinematics.SwerveModuleState.optimize(swerveModuleStates[3], self.backRight.getEncoder())])

        self.frontLeft.setDesiredState(swerveModuleStates[0])
        self.frontRight.setDesiredState(swerveModuleStates[1])
        self.backLeft.setDesiredState(swerveModuleStates[2])
        self.backRight.setDesiredState(swerveModuleStates[3])

    def setMaxOutput(self, maxOutput):
        self.maxOut = maxOutput
