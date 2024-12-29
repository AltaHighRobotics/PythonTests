from utils.stateManager import StateManager
import constants

class MasterState(StateManager):
    """
    Handles all button input
    """
    def __init__(self):
        self.target = None