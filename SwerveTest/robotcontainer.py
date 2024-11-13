#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import wpilib
from wpilib.interfaces import GenericHID

import commands2
import commands2.button

import constants
from subsystems.state import State
from subsystems.swerveDrive import SwerveDrive
from commands.FCDrive import FODrive
from commands.RODrive import RODrive
from commands.halveDriveSpeed import HalveDriveSpeed

class RobotContainer:
    """
    This class is where the bulk of the robot should be declared. Since Command-based is a
    "declarative" paradigm, very little robot logic should actually be handled in the :class:`.Robot`
    periodic methods (other than the scheduler calls). Instead, the structure of the robot (including
    subsystems, commands, and button mappings) should be declared here.
    """

    def __init__(self) -> None:
        # The driver's controller
        # self.driverController = wpilib.XboxController(constants.kDriverControllerPort)
        self.driverController = wpilib.Joystick(constants.kDriverControllerPort)

        # The robot's subsystems        
        # State
        self.state = State()
        
        # Drive
        self.drive = SwerveDrive()

        # Chooser
        self.chooser = wpilib.SendableChooser()

        # Add commands to the autonomous command chooser
        self.chooser.setDefaultOption("Simple Auto", 'A')
        self.chooser.addOption("Complex Auto", 'B')

        # Put the chooser on the dashboard
        wpilib.SmartDashboard.putData("Autonomous", self.chooser)

        self.configureButtonBindings()
        self.drive.setDefaultCommand(
            FODrive(self.drive,
                self.driverController.getX, 
                self.driverController.getY, 
                self.driverController.getZ
                )
        )

        # set up default drive command

    def mapButton(self, button, stateTrigger): # Maps a physical button to trigger a state change
        commands2.button.JoystickButton(self.driverController, button).onTrue(commands2.cmd.runOnce(lambda: self.state.handleButton(stateTrigger, True))).onFalse(commands2.cmd.runOnce(lambda: self.state.handleButton(stateTrigger, False)))

    def configureButtonBindings(self):
        """
        Use this method to define your button->command mappings. Buttons can be created by
        instantiating a :GenericHID or one of its subclasses (Joystick or XboxController),
        and then passing it to a JoystickButton.
        """
        # BUTTONS - Buttons trigger states or commands
        self.mapButton(1, 'a')
        self.mapButton(2, 'b')
        self.mapButton(3, 'c')
        self.mapButton(4, 'd')

        # STATES - States trigger commands
        commands2.button.Trigger(self.state.isDriveFO).whileTrue(
            FODrive(self.drive,
                    self.driverController.getX, 
                    self.driverController.getY, 
                    self.driverController.getZ
                    )
                    ).whileFalse(
                     RODrive(self.drive,
                            self.driverController.getX, 
                            self.driverController.getY, 
                            self.driverController.getZ
                    )   
                    )
        
        commands2.button.Trigger(self.state.isDriveHalfSpeed).whileTrue(HalveDriveSpeed(self.drive))
        
    def getAutonomousCommand(self) -> str:
        return self.chooser.getSelected()
