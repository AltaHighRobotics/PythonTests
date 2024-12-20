import wpilib
from photonlibpy.photonCamera import PhotonCamera
import time

class MyRobot(wpilib.TimedRobot):
    def robotInit(self) -> None:
        self.cam = PhotonCamera("camera1")
    
    def teleopInit(self) -> None:
        self.lastTime = time.time()
    def teleopPeriodic(self) -> None:

        # Get information from the camera
        result = self.cam.getLatestResult()
        if result.hasTargets():
            for target in result.getTargets():
                print(target.getFiducialId())
                self.lastTime = time.time()