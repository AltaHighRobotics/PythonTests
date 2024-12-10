import math

# Input
kDriverControllerPort = 0

# States
kDefaultObjective = "I"
kDefaultBucket = 0
kDefaultIntake = 0
kDefaultEndStop = -1
kDefaultEndStopOverride = 0

# Swerve
kModuleMaxAngularVelocity = math.pi
kModuleMaxAngularAcceleration = math.tau
kSwerveTurnGearRatio = 1/37

# Dimensions
kSwerveModCtrToCtr = .635
kWheelRadius = 0.0508

# Enstops
kOutEndstopPort = 1
kInEndstopPort = 1
kEndstopInversion = False

# Speeds
kBucketSpeed = .8
kIntakeSpeed = .8
kOuttakeSpeed = .3
kSwerveMinSpeed = .2
kSwerveMaxSpeed = 1
kSwerveMaxOutput = .8
# MotorIDs
# Bucket
kBucketID = 9

#Intake
kIntakeLID = 10
kIntakeRID = 11

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

# Turn PID
# Front Left
kTurnFLP = 15
kTurnFLI = 0
kTurnFLD = .1

# Front Right
kTurnFRP = kTurnFLP + 0
kTurnFRI = kTurnFLI + 0
kTurnFRD = kTurnFLD + 0

# Back Left
kTurnBLP = kTurnFLP + 0
kTurnBLI = kTurnFLI + 0
kTurnBLD = kTurnFLD + 0

# Back Right
kTurnBRP = kTurnFLP + 0
kTurnBRI = kTurnFLI + 0
kTurnBRD = kTurnFLD + 0

