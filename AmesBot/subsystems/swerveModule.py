import math
import wpilib
import wpimath.kinematics
import wpimath.geometry
import wpimath.controller
import wpimath.trajectory
import rev
import phoenix5 as ctre
import constants


kWheelRadius = 0.0508
kModuleMaxAngularVelocity = math.pi
kModuleMaxAngularAcceleration = math.tau


class SwerveModule:
    def __init__(self, driveid, steerid, kP, kI, kD):
        self.drive = ctre.WPI_TalonSRX(driveid)
        self.turn = rev.CANSparkMax(steerid, rev.CANSparkLowLevel.MotorType.kBrushless)
        self.turnEncoder = self.turn.getEncoder()
        self.turnEncoder.setPositionConversionFactor(constants.kSwerveTurnDisPerPulse/42)
        self.turningPIDController = wpimath.controller.ProfiledPIDController(
            kP,
            kI,
            kD,
            wpimath.trajectory.TrapezoidProfile.Constraints(
                kModuleMaxAngularVelocity,
                kModuleMaxAngularAcceleration,
            ),
        )
        self.drive.setNeutralMode(ctre.NeutralMode.Brake) # Brake

        # Limit input range to -pi to pi with wrap
        self.turningPIDController.enableContinuousInput(-math.pi, math.pi)

    def setDesiredState(
        self, desiredState: wpimath.kinematics.SwerveModuleState
    ) -> None:
        """Sets the desired state for the module.

        :param desiredState: Desired state with speed and angle.
        """

        encoderRotation = wpimath.geometry.Rotation2d(self.turningEncoder.getDistance())

        # Optimize the reference state to avoid spinning further than 90 degrees
        state = wpimath.kinematics.SwerveModuleState.optimize(
            desiredState, encoderRotation
        ) # Remove if dirve motors are jittering

        # Scale speed by cosine of angle error. This scales down movement perpendicular to the desired
        # direction of travel that can occur when modules change directions. This results in smoother
        # driving.
        state.speed *= (state.angle - encoderRotation).cos() # Remove if motors are going the wrong way

        # Calculate the drive output from the drive PID controller.
        driveOutput = state.speed

        # Calculate the turning motor output from the turning PID controller.
        turnOutput = self.turningPIDController.calculate(
            self.turnEncoder.getPosition(), -state.angle.radians()
        )

        self.drive.set(driveOutput)
        self.turn.setVoltage(turnOutput)

        
        