from photonlibpy.photonCamera import PhotonCamera
from commands2 import Subsystem
import constants
from photonlibpy.photonTrackedTarget import PhotonTrackedTarget
from utils.flag import Flag

class AprilTagSubsystem(Subsystem): # Apriltags with PhotonVision
    def __init__(self) -> None:
        super().__init__()

        self.cam = PhotonCamera(constants.kCamName)
        self.flagOn = False
        self.flag = None

    def getHighestID(self, targets: list[PhotonTrackedTarget]) -> PhotonTrackedTarget: # get the target with the highest fiducial ID
        bestTarget = targets[0]
        for target in targets:
            if target.getFiducialId() > bestTarget.getFiducialId():
                bestTarget = target
        return bestTarget

    def getTargets(self) -> list[PhotonTrackedTarget]: # Get latest target data
        result = self.cam.getLatestResult()
        if result.hasTargets():
            return result.getTargets()
        else: return None
    
    def hasTarget(self, id: int = None) -> bool: # See if a target with a given fiducial is visible. Run with no args to see if any targets are visible
        targets = self.getTargets()
        if targets is not None:
            if id is not None: 
                for target in targets:
                    if target.getFiducialId() == id:
                        return True # If target is found
            else: return True # If no id is given and we have targets
        return False # No targets
    
    def getTargetSteer(self, id:int): # Get a steer value to steer the bot towards a target
        targets = self.getTargets()
        if targets is not None:
            for target in targets:
                if target.getFiducialId() == id:
                    return target.getYaw()/30
        return 0
    
    def setFlag(self, flag: Flag):
        self.flagOn = True
        self.flag = flag

    def isFlagged(self):
        return self.flagOn
