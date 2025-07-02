from items import *
from locations import *
    
class PlayerCharacter:
    def __init__(self, location: GameLocation, inventory: list[GameItem]):
        self.location = location
        self.inventory = inventory
        
class PlayerInstance:
    player: PlayerCharacter = None
    start_location = next(loc for loc in GameLocation.all_locations() if loc.location_type == LocationType.lighthouse)
    
    @staticmethod
    def init_player():
        PlayerInstance.player = PlayerCharacter(location=PlayerInstance.start_location, inventory=[])

PlayerInstance().init_player()