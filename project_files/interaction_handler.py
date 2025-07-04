from npc import *
from items import GameItem
from locations import GameLocation
from player import *
from game_state import *
from dialogue_handler import *

class Commands:
    def inventory(self, items: list[GameItem]):
        if not items:
            return "Your inventory is empty."
        return "Inventory: " + "-".join(f"{item.name}" for item in items)
    def info(self):
        print("info called")
        self.commands = ['inventory', 'help', 'go to [location]', 'pick up [item]', 'drop [item]', 'inspect [item/location/person]', 'talk to [name]', 'ask [name] about [topic(person/item/location)]', 'attack [name]']
        return "Available commands: " + "".join(f"- {cmd}." for cmd in self.commands)
    #--navigation--
    def navigate(self, location: GameLocation):
        if location:
            if PlayerInstance.player.location.location_type == LocationType.cave:
                if location.location_type != LocationType.cave:
                    return "The song grow louder and you hear her voice echo through the cave. Where do you think you're going?" 
                
            PlayerInstance.player.location = location
            if location.location_type == LocationType.cave:
                return f"You go to the {location.name}. {location.description} You know you don't stand a chance unless you can attack before the song overwhelms you."
        
            return f"You go to the {location.name}. {location.description}"
    #--npc interaction--
    def talk(self, npc: NPCInterface):
        return DialogueHandler.talk_to(npc.name)
    def ask_about(self, npc: NPCInterface, topic):
        return DialogueHandler.ask_about(npc.name, topic)
    def attack(self, npc: NPCInterface):
        if not npc.isFriendly and any(item.name == 'knife' for item in PlayerInstance.player.inventory):
            if npc.npc_type == NPCType.siren:
                state.active_flags.add(GameFlag.won_game)
            return f"You draw your knife from its sheath, catching them off guard, and take them down in one fatal swipe."
        elif npc.isFriendly:
            return "You cannot attack a friend."
        else:
            if npc.npc_type == NPCType.siren:
                state.active_flags.add(GameFlag.lost_game)
            return "You attempt to attack them, but find you have no weapon. Without one, you don't stand a chance."
    #--item interaction--
    def pick_up(self, item: GameItem):
        if not isinstance(item, GameItem):
            return "Invalid item."

        if not item.isInteractable:
            return "You cannot pick up this item."
        # add item to inventory if it is interactable, else tell player not interactable
        #update game state based on interaction
        for loc_item in PlayerInstance.player.location.items:
            if loc_item and loc_item.isInteractable:
                if loc_item.name.lower() == item.name.lower():
                    if item.item_type == ItemType.artifact:
                        state.active_flags.add(GameFlag.found_artifact)
                    elif item.item_type == ItemType.journal:
                        state.active_flags.add(GameFlag.found_journal)
                    elif item.item_type == ItemType.sapphire_bracelet:
                        state.active_flags.add(GameFlag.found_bracelet)
                    elif item.item_type == ItemType.shrine:
                        state.active_flags.add(GameFlag.found_shrine)
                    elif item.item_type == ItemType.knife:
                        state.active_flags.add(GameFlag.found_knife)
                    PlayerInstance.player.inventory.append(loc_item)
                    PlayerInstance.player.location.items.remove(loc_item)
                    return f'You pick up the {item}.'
        return "That item is not in your location."
    def drop(self, item: GameItem):
        for inv_item in PlayerInstance.player.inventory:
            if inv_item.name == item.name:
                PlayerInstance.player.inventory.remove(inv_item)
                PlayerInstance.player.location.items.append(inv_item)
                return f'You drop the {item.name}.'
        return "You do not have that item."
    def inspect(self, thing):
        desc = getattr(thing, 'description', None)

        if not desc:
            return "There is nothing special about it."

        # If the description is a list, join it
        if isinstance(desc, list):
            return "\n".join(str(line).strip() for line in desc if str(line).strip())

        # If it's a string, return it
        if isinstance(desc, str):
            return desc.strip()

class InputHandler:
    def __init__(self):
        self.commands = Commands()

    def handle_command(self, command):
        self.cmd = command.strip("> ").lower()

        #--navigation
        if self.cmd.startswith('go to'):
            location_name = self.cmd[6:].strip().lower()
            location = GameLocation.get_by_name(location_name)
            if location:
                return self.commands.navigate(location)
            return "That location does not exist."
        #--system commands
        elif self.cmd.startswith('inventory'):
            return self.commands.inventory(PlayerInstance.player.inventory)
        elif self.cmd.startswith('help'):
            return self.commands.info()
        #--item interaction--
        elif self.cmd.startswith('pick up'):
            item_name = self.cmd[7:].strip().lower()
            item = GameItem.get_by_name(item_name)
            if item is None:
                return "That item does not exist."
            return self.commands.pick_up(item)
        elif self.cmd.startswith('drop'):
            item_name = self.cmd[4:].strip().lower()
            item = GameItem.get_by_name(item_name)
            if item.name.lower() == item_name.lower():
                return self.commands.drop(item)
            return "You do not have that item."
        elif self.cmd.startswith('inspect'):
            input_name = self.cmd[7:].strip().lower()
            inventory_items = PlayerInstance.player.inventory
            location_items = PlayerInstance.player.location.items
            location_npcs = PlayerInstance.player.location.npcs
            #loops through inventory items, if none found loops location items, if none found checks  current location valid
            for item in inventory_items:
                if input_name.strip().lower() == item.name.lower():
                    return self.commands.inspect(item)
            for item in location_items:
                if input_name.strip().lower() == item.name.strip().lower():
                    return self.commands.inspect(item)
            for npc in location_npcs:
                if input_name.strip().lower() == npc.name.strip().lower():
                    return self.commands.inspect(npc)
            if PlayerInstance.player.location.name.strip().lower() == input_name:
                return self.commands.inspect(PlayerInstance.player.location)
            return "There's nothing special about it."

        #--npc interaction--
        elif self.cmd.startswith('attack'):
            npc_name = self.cmd[6:].strip().lower()
            npc = NPC.get_by_name(npc_name)
            if npc:
                return self.commands.attack(npc)
            return "You can not attack that person, or they are not in your location, or they do not exist."
        elif self.cmd.startswith('talk to'):
            npc_name = self.cmd[7:].strip().lower()
            npc = NPC.get_by_name(npc_name)
            if npc:
                for loc_npc in PlayerInstance.player.location.npcs:
                    if loc_npc.name.lower() == npc.name.lower():
                        return self.commands.talk(npc)
            return f"{npc_name.capitalize()} is not in your location or does not exist."
            
        elif self.cmd.startswith('ask'):
            #remove prefix, then split the command to access the elements
            input_str = self.cmd[4:].strip().lower()
            if ' about ' in input_str:
                npc_name, topic = input_str.split(' about ', 1)
                npc_name = npc_name.strip().lower()
                topic = topic.strip().lower()
                npc = NPC.get_by_name(npc_name)

                if npc:
                    for loc_npc in PlayerInstance.player.location.npcs:
                        return self.commands.ask_about(npc, topic)
                return f"{npc_name.capitalize()} doesn't have anything to say about the {topic}."
            else:
                return "Please format your question 'ask [name] about [topic]"
        else:
            return "Command not recognized. Type 'help' for help"