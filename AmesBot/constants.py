import math

# Input
kDriverControllerPort = 0
kDeadband = .2

# States
kDefaultObjective = "I"
kDefaultBucket = 0
kDefaultIntake = 0
kDefaultEndStop = -1
kDefaultEndStopOverride = 0

# Swerve
kModuleMaxAngularVelocity = math.tau
kModuleMaxAngularAcceleration = 2*math.tau
kSwerveTurnGearRatio = 1/37

# Dimensions
kSwerveModCtrToCtr = .635
kWheelRadius = 0.0508

# Enstops
kOutEndstopPort = 3
kInEndstopPort = 2
kEndstopInversion = True

# Speeds
kBucketSpeed = .9
kIntakeSpeed = .7
kOuttakeSpeed = .4
kSwerveMinSpeed = .3
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
kTurnFLP = 10
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

