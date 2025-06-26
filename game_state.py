from enum import Enum

class GameFlag(Enum):
    found_bracelet = 1
    found_journal = 2
    found_artifact = 3
    found_shrine = 4
    NONE = 5

#--track game state--
class GameState:
    def __init__(self):
        self.active_flags = set()