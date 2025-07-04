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

    def __str__(self):
        return self.name

    @staticmethod
    def all_npcs() -> dict[NPCType, NPCInterface]:
        return {
            NPCType.siren: NPC("siren", NPCType.siren, "Her stature is surprisingly tall and intimidating for her size, and you know immediately that she must be a siren. She is ethereal with glistening pale skin and limbs too long for her body. Her stillness is unnerving, like she's waiting for a cue only she can hear.", False),
            NPCType.sailor: NPC("sailor", NPCType.sailor, "Broad and weathered, with a crooked nose, one milky eye, and rope-burned hands, he seems paranoid, twitchy, and always his good eye is always darting from place to place.", True),
            NPCType.hermit: NPC("hermit", NPCType.hermit, "He is a wiry, sunburnt old man with wild white hair and shadowed eyes, making him look almost ancient. He speaks slowly, as if time bends around him.", True),
            NPCType.bartender: NPC("bartender", NPCType.bartender, "He is a thick-built man, and bald with faded tattoos and calloused hands. He is calm, quiet, and always seems to be watching everything at once from the corner of his eye.",  True),
            NPCType.marla: NPC("Marla", NPCType.marla, "She's young, with thin sharp eyes, wrapped in an oversized coat with unevenly cut hair. Her appearance seems a bit odd, although looking around you notice that many other people here do too.", True)
        }
    
    @staticmethod
    def get_by_name(name: str) -> NPCInterface | None:
        return next((npc for npc in NPC.all_npcs().values() if npc.name.lower() == name.lower()), None)
    