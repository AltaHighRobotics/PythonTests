#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import commands2
import wpilib
import wpilib.drive
import phoenix5 as ctre

import constants


class DriveSubsystem(commands2.Subsystem):
    def __init__(self) -> None:
        super().__init__() 
        self.left1 = ctre.WPI_TalonFX(constants.kLeftMotor1ID)
        self.left2 = ctre.WPI_TalonFX(constants.kLeftMotor2ID)
        self.right1 = ctre.WPI_TalonFX(constants.kRightMotor1ID)
        self.right2 = ctre.WPI_TalonFX(constants.kRightMotor2ID)

        self.left1.setNeutralMode(ctre.NeutralMode.Brake)
        self.left2.setNeutralMode(ctre.NeutralMode.Brake)
        self.right1.setNeutralMode(ctre.NeutralMode.Brake)
        self.right2.setNeutralMode(ctre.NeutralMode.Brake)

        self.left = wpilib.MotorControllerGroup(self.left1, self.left2)
        self.right = wpilib.MotorControllerGroup(self.right1, self.right2)

        self.left.setInverted(True)
        # The robot's drive
        self.drive = wpilib.drive.DifferentialDrive(
            self.left,
            self.right,
            )
        self.maxOut = .5
        self.drive.setMaxOutput(.5)

    def arcadeDrive(self, fwd: float, rot: float) -> None:
        """
        Drives the robot using arcade controls.

        :param fwd: the commanded forward movement
        :param rot: the commanded rotation
        """

        self.drive.arcadeDrive(fwd, rot)

    def setMaxOutput(self, maxOutput: float):
        """
        Sets the max output of the drive. Useful for scaling the
        drive to drive more slowly.
        """
        self.maxOut = maxOutput
        self.drive.setMaxOutput(maxOutput)