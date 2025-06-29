from enum import Enum

class GameFlag(Enum):
    found_bracelet = 1
    found_journal = 2
    found_artifact = 3
    found_shrine = 4
    found_knife = 5
    won_game = 6
    lost_game = 7
    NONE = 8

#--track game state--
class GameState:
    def __init__(self):
        self.active_flags = set()

state = GameState()