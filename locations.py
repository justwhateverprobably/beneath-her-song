from typing import Protocol
from enum import Enum
from items import *
from npc import *
from abc import abstractmethod

class LocationType(Enum):
    lighthouse = 0
    docks = 1
    beach = 2
    tavern = 3
    forest = 4
    cave = 5

class GameLocationInterface(Protocol):
    name: str
    location_type: LocationType
    description: str
    items: list[GameItemInterface]
    npcs: list[NPCInterface]
    
class GameLocation:
    def __init__(self, name: str, location_type: LocationType, description: str, items: list[GameItemInterface], npcs: list[NPCInterface]):
        self.name = name
        self.location_type = location_type
        self.description = description
        self.items = items
        self.npcs = npcs

    @staticmethod
    def all_locations() -> list[GameLocationInterface]:
        items = GameItem.all_items()
        npcs = NPC.all_npcs()
        return[
            GameLocation("lighthouse", LocationType.lighthouse, "A lone beacon that sits atop a small hill on the outskirts of the village, shrouded in the fog. The familiar walls shelter you from the howling wind and harsh waves.", [items[ItemType.coins]], []),
            GameLocation("docks", LocationType.docks, "The rickety boards stretch out into the ocean, and seem to disappear in the heavy mist. Boats groan as they rock back and forth in the water, as if heaving one final breath.", [items[ItemType.journal], items[ItemType.knife]], [npcs[NPCType.sailor]]),
            GameLocation("beach", LocationType.beach, "The smell of salt and fish is unmistakable. Sometimes you can almost taste it. Waves lap gently onto the shore, and bring with them a melody that seems to float on the wind.", [items[ItemType.sapphire_bracelet]], []),
            GameLocation("tavern", LocationType.tavern, "'The warm flickering light of the lanterns beckon you in, and familiar voices drift past your ears as you enter.'", [], [npcs[NPCType.bartender], npcs[NPCType.marla]]),
            GameLocation("forest", LocationType.forest, "The dense cover of trees shrouds you in shadow, and seems to block out everything but the sound of your own breath and twigs snapping under your feet. The stillness has an almost ethereal feel to it.", [items[ItemType.shrine], items[ItemType.artifact]], [npcs[NPCType.hermit]]),
            GameLocation("cave", LocationType.cave, "Tucked into the side of the cliff, the entrance to the cave gapes like the mouth of some ancient monster frozen in time. The muddled sounds of the sea echo inside, and create a hauntingly beautiful tone.", [], [npcs[NPCType.siren]]),
        ]