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
kTurnFLP = 1
kTurnFLI = 0
kTurnFLD = 0
kTurnFLS = 1
kTrunFLV = .5

# Front Right
kTurnFRP = 1
kTurnFRI = 0
kTurnFRD = 0
kTurnFRS = 1
kTrunFRV = .5

# Back Left
kTurnBLP = 1
kTurnBLI = 0
kTurnBLD = 0
kTurnBLS = 1
kTrunBLV = .5

# Back Right
kTurnBRP = 1
kTurnBRI = 0
kTurnBRD = 0
kTurnBRS = 1
kTrunBRV = .5

# Swerve
kModuleMaxAngularVelocity = math.pi
kModuleMaxAngularAcceleration = math.tau
kSwerveTurnGearRatio = 1