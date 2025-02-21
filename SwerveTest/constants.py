import math

# Input
kDriverControllerPort = 0

# States
kDefaultDriveMode = "FO"
kDefaultDriveSide = "F"
kDefaultIsHalfSpeed = False

# Dimensions
kSwerveModCtrToCtr = .635
kWheelRadius = 0.0508

# MotorIDs
# Front Left
kFLDriveID = 1
kFLTurnID = 2

# Front Right
kFRDriveID = 3
kFRTurnID = 4

# Front Left
kBLDriveID = 5
kBLTurnID = 6

# Front Right
kBRDriveID = 7
kBRTurnID = 8

# Turn PID % FF
# Front Left
kTurnFLP = 10
kTurnFLI = 0
kTurnFLD = 0

# Front Right
kTurnFRP = 10
kTurnFRI = 0
kTurnFRD = 0

# Back Left
kTurnBLP = 10
kTurnBLI = 0
kTurnBLD = 0

# Back Right
kTurnBRP = 10
kTurnBRI = 0
kTurnBRD = 0

# Swerve
kModuleMaxAngularVelocity = math.pi
kModuleMaxAngularAcceleration = math.tau
kSwerveTurnGearRatio = 1/(11.3142 * 3)