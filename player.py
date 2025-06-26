from items import *
from locations import *
    
class PlayerCharacter:
    def __init__(self, location: GameLocation, inventory: list[GameItem]):
        self.location = location
        self.inventory = inventory
        
class PlayerInstance:
    player: PlayerCharacter = None
    
    @staticmethod
    def init_player():
        start_location = next(loc for loc in GameLocation.all_locations() if loc.location_type == LocationType.lighthouse)
        PlayerInstance.player = PlayerCharacter(location=start_location, inventory=[])