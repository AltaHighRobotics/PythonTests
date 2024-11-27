# TODO: insert robot code here
import commands2

from robotContainer import robotContainer

class myRobot(commands2.TimedCommandRobot):

    def robotInit(self) -> None:

        self.containter = robotContainer()

