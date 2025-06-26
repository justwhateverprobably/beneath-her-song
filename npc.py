from typing import Protocol
from enum import Enum

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
    def __init__(self, name: str, npc_type: NPCType, dialogues):
        self.name = name
        self.npc_type = npc_type
        self.dialogues = dialogues

    @staticmethod
    def all_npcs() -> list[NPCInterface]:
        siren_dialogue = []
        hermit_dialogue = []
        sailor_dialogue = []
        bartender_dialogue = []
        marla_dialogue = []
        return [
            NPC("siren", NPCType.siren, siren_dialogue),
            NPC("sailor", NPCType.sailor, sailor_dialogue),
            NPC("hermit", NPCType.hermit, hermit_dialogue),
            NPC("bartender", NPCType.bartender, bartender_dialogue),
            NPC("Marla", NPCType.marla, marla_dialogue)
        ]