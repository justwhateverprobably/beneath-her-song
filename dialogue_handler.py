from game_state import *

siren_dialogue_map = {
    GameFlag.found_artifact: "",
    GameFlag.found_bracelet: "",
    GameFlag.found_journal: "",
    GameFlag.found_shrine: "",
    'default': "You hear the voice calling to you, stronger than ever now, and in the distance you see her...She turns her head and beckons you closer, her voice captivating you as she speaks."
}
sailor_dialogue_map = {
    GameFlag.found_artifact: "",
    GameFlag.found_bracelet: "",
    GameFlag.found_journal: "",
    GameFlag.found_shrine: "",
    'default': ""
}
marla_dialogue_map = {
    GameFlag.found_artifact: "",
    GameFlag.found_bracelet: "",
    GameFlag.found_journal: "",
    GameFlag.found_shrine: "",
    'default': ""
}
bartender_dialogue_map = {
    GameFlag.found_artifact: "",
    GameFlag.found_bracelet: "",
    GameFlag.found_journal: "",
    GameFlag.found_shrine: "",
    'default': ""
}
hermit_dialogue_map = {
    GameFlag.found_artifact: "",
    GameFlag.found_bracelet: "",
    GameFlag.found_journal: "",
    GameFlag.found_shrine: "",
    'default': ""
}

dialogue_maps = {
    'siren': siren_dialogue_map,
    'hermit': hermit_dialogue_map,
    'sailor': sailor_dialogue_map,
    'marla': marla_dialogue_map,
    'bartender': bartender_dialogue_map,
    'default': "You don't know anyone by that name."
}

class DialogueHandler:
    def get_dialogue(npc_name) -> list[str]:
        dialogue_map = dialogue_maps.get(npc_name)
        flags = state.active_flags
        lines = []

        if not dialogue_map:
            return [f"You don't know anyone named {npc_name}."]
        
        for flag, line in dialogue_map.items():
            if flag == 'default':
                continue
            if flag in flags:
                lines.append(line)

        if not lines:
            lines.append(dialogue_map.get('default'))

        return lines