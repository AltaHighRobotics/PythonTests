import math

# Input
kDriverControllerPort = 0

# States
#kDefaultDriveMode = "FO"
#kDefaultDriveSide = "F"
#kDefaultIsHalfSpeed = False
kDefaultObjective = "I"
kDefaultBucket = 0
kDefaultIntake = 0
kDefaultEndStop = 0
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
kBucketSpeed = .5
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

# Turn PID % FF
# Front Left
kTurnFLP = 15
kTurnFLI = 0
kTurnFLD = .1

# Front Right
kTurnFRP = 15
kTurnFRI = 0
kTurnFRD = .1

# Back Left
kTurnBLP = 15
kTurnBLI = 0
kTurnBLD = .1

# Back Right
kTurnBRP = 15
kTurnBRI = 0
kTurnBRD = .1

