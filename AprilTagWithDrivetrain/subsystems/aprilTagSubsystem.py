from asyncio import constants
from photonlibpy.photonCamera import PhotonCamera
from commands2 import Subsystem
import constants

class AprilTagSubsystem(Subsystem):
    def __init__(self) -> None:
        self.cam = PhotonCamera(constants.kCamName)

    def getTargets(self):
        result = self.cam.getLatestResult()
        if result.hasTargets():
            return result.getTargets()
        else: return None
    
    def hasTarget(self, id: int) -> bool:
        targets = self.getTargets()
        if targets is not None:
            for target in targets:
                if target.getFiducialId() == id:
                    return True
        return False
    
    def getTargetSteer(self, id:int):
        targets = self.getTargets()
        if targets is not None:
            for target in targets:
                if target.getFiducialId() == id:
                    return target.getYaw()/30
        return 0