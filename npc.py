from typing import Protocol
from enum import Enum
from game_state import *

class NPCType(Enum):
    siren = 0
    sailor = 1
    hermit = 2
    bartender = 3
    marla = 4

class NPCInterface(Protocol):
    name: str
    npc_type: NPCType
    dialogues: list


class NPC():
    def __init__(self, name: str, npc_type: NPCType):
        self.name = name
        self.npc_type = npc_type

    @staticmethod
    def all_npcs() -> dict[NPCType, NPCInterface]:
        return {
            NPCType.siren: NPC("siren", NPCType.siren),
            NPCType.sailor: NPC("sailor", NPCType.sailor),
            NPCType.hermit: NPC("hermit", NPCType.hermit),
            NPCType.bartender: NPC("bartender", NPCType.bartender),
            NPCType.marla: NPC("Marla", NPCType.marla)
        }
    
    @staticmethod
    def get_by_name(name: str) -> NPCInterface | None:
        return next((npc for npc in NPC.all_npcs() if npc.name.lower() == name.lower()), None)
    