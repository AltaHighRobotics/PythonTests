import wpilib
import commands2.button

import constants

from commands.driveCommand import DriveCommand
from commands.halveDriveSpeed import HalveDriveSpeed
from subsystems.driveSubsystem import DriveSubsystem

class robotContainer:
    
    def __init__(self):
        self.controller = wpilib.Joystick(constants.KDriveControllerPort)

        self.drive = DriveSubsystem()

        self.drive.setDefaultCommand(DriveCommand(self.drive, lambda: -self.controller.getY(), lambda: self.controller.getZ()))

        self.configureBindings()

    def configureBindings(self):
        commands2.button.JoystickButton(self.controller, 2).whileTrue(HalveDriveSpeed(self.drive))




            


