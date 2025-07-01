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
    isFriendly: True


class NPC():
    def __init__(self, name: str, npc_type: NPCType, description,  isFriendly: bool):
        self.name = name
        self.npc_type = npc_type
        self.description = description
        self.isFriendly = isFriendly

    @staticmethod
    def all_npcs() -> dict[NPCType, NPCInterface]:
        return {
            NPCType.siren: NPC("siren", NPCType.siren, "Tall and ethereal with glistening pale skin and limbs too long. Her stillness is unnerving, like she's waiting for a cue only she can hear.", False),
            NPCType.sailor: NPC("sailor", NPCType.sailor, "Broad and weathered, with a crooked nose, one milky eye, and rope-burned hands. Paranoid, twitchy, and always scanning the horizon.", True),
            NPCType.hermit: NPC("hermit", NPCType.hermit, "He is a wiry, sunburnt old man with wild white hair and shadowed eyes. He speaks slowly, as if time bends around him.", True),
            NPCType.bartender: NPC("bartender", NPCType.bartender, "He is a thick-built and bald with faded tattoos and calloused hands. Calm, quiet, and always watching from the corner of his eye.",  True),
            NPCType.marla: NPC("Marla", NPCType.marla, "Thin and sharp-eyed, wrapped in an oversized coat with unevenly cut hair. She scribbles in a notebook mid-sentence, like you're part of a theory.", True)
        }
    
    @staticmethod
    def get_by_name(name: str) -> NPCInterface | None:
        return next((npc for npc in NPC.all_npcs() if npc.name.lower() == name.lower()), None)
    