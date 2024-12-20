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