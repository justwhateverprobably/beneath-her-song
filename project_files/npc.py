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
            NPCType.siren: NPC("siren", NPCType.siren, "She has a snake-like stature and is surprisingly intimidating for her size, and you know immediately that she must be a siren. She is ethereal with glistening pale skin and limbs too long for her body, yet still captivates you. Her stillness is unnerving, like she's waiting for a cue only she can hear.", False),
            NPCType.sailor: NPC("sailor", NPCType.sailor, "Broad and weathered, with a crooked nose, short grey hair, and tattered clothes, he seems paranoid, twitchy, and always his one good eye is always darting from place to place.", True),
            NPCType.hermit: NPC("hermit", NPCType.hermit, "He is a short, wiry, suntanned old man with a bald head and scraggly beard. His eyes look sunken and shadowed, making him look almost ancient. He mutters slowly to himself, as if time bends around him.", True),
            NPCType.bartender: NPC("bartender", NPCType.bartender, "He is a thick-built man, with faded tattoos covering his head and a gruff look on his face. He is calm, quiet, and always seems to be busy doing various tasks, or exchanging small talk.",  True),
            NPCType.marla: NPC("Marla", NPCType.marla, "She's young, with thin sharp eyes, wrapped in an oversized coat with unevenly cut hair. Her appearance seems a bit odd, although looking around you notice that many other people here do too.", True)
        }
    
    @staticmethod
    def get_by_name(name: str) -> NPCInterface | None:
        return next((npc for npc in NPC.all_npcs().values() if npc.name.lower() == name.lower()), None)
    