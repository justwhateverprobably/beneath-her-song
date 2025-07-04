from typing import Protocol
from abc import abstractmethod

from game_state import *

class ItemType(Enum):
    coins = 0
    knife = 1
    sapphire_bracelet = 2
    journal = 3
    artifact = 4
    shrine = 5

class GameItemInterface(Protocol):
    name: str
    item_type: ItemType
    description: str
    isInteractable: bool
    flag: GameFlag

class GameItem:
    def __init__(self, name: str, item_type: ItemType, description: str, isInteractable: bool, flag: GameFlag):
        self.name = name
        self.item_type = item_type
        self.description = description
        self.isInteractable = isInteractable
        self.flag = flag

    def __str__(self):
        return self.name
    
    @staticmethod
    def all_items() -> dict[ItemType, GameItemInterface]:
        return{
            ItemType.coins: GameItem('coins', ItemType.coins, "They glint faintly in the light.", True, GameFlag.NONE),
            ItemType.knife: GameItem('knife', ItemType.knife, 'It has a hefty feel to it, and you assume it has had years of use based on its condition. Nevertheless, it seems sturdy, and you figure you might be able to use it at some point', True, GameFlag.NONE),
            ItemType.sapphire_bracelet:GameItem('sapphire bracelet', ItemType.sapphire_bracelet, "It's cold to the touch, and seems to pulse faintly. It has and inexplicable air to it, and seems almost to call to you, although you're unsure. You take note of the fine craftsmanship and the beautiful glow of the sapphire in the dim light, and you wonder who it could have belonged to, or where it could have come from.", True, GameFlag.found_bracelet),
            ItemType.journal: GameItem('journal', ItemType.journal, "The leather cover and old pages look worn from years of travel and frequent use. You flip through the pages for a while, and find many mentions of strange dreams, cryptic warnings, mysterious inlets and caves, and faint melodies on the water scattered throughout tales of grand adventures out at sea.", True, GameFlag.found_journal),
            ItemType.artifact: GameItem('artifact', ItemType.artifact, "Half buried in the earth, you pick up a smooth stone with mysterious runes etched into the surface, similar to those on the shrine. You wonder what it could mean", True, GameFlag.found_artifact),
            ItemType.shrine: GameItem('shrine', ItemType.shrine, "The ancient moss covered stone juts out from the ground, etched with cryptic carvings in it's surface.", False, GameFlag.found_shrine),
        }
    
    @staticmethod
    def get_by_name(name: str) -> GameItemInterface | None:
        return next((item for item in GameItem.all_items().values() if item.name.lower() == name.lower()), None)