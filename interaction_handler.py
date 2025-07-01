from npc import *
from items import GameItem
from locations import GameLocation
from player import *
from game_state import *
from dialogue_handler import *

class Commands:
    def inventory(self, items: list[GameItem]):
        self.inventory = items
        return str(self.inventory)
    def info(self):
        self.commands = ['inventory', 'help', 'go to [location]', 'pick up [item]', 'drop [item]', 'use [item]', 'inspect [item/location]', 'talk to [name]', 'ask [name] about [topic]', 'attack [name]']
        return str(self.commands)
    #--navigation--
    def navigate(self, location: GameLocation):
        self.location = location
        PlayerInstance.player.location = self.location
        return f"You go to the {self.location.name}."
    #--npc interaction--
    def talk(self, npc: NPCInterface):
        return DialogueHandler.talk_to(npc.name)
    def ask_about(self, npc: NPCInterface, topic):
        return DialogueHandler.ask_about(npc.name, topic)
    def attack(self, npc: NPCInterface):
        self.npc = npc
        self.npc_name = self.npc.name
        if not self.npc.isFriendly and GameItem.get_by_name('knife') in PlayerInstance.player.inventory:
            if self.npc.npc_type == NPCType.siren:
                state.active_flags.add(GameFlag.won_game)
            return f"You draw your knife from its sheath, and attack them viciously."
        elif self.npc.isFriendly:
            return "You cannot attack a friend."
        else:
            if self.npc.npc_type == NPCType.siren:
                state.active_flags.add(GameFlag.lost_game)
            return "You attempt to attack them, but find you have no weapon. Without one, you don't stand a chance."
    #--item interaction--
    def pick_up(self, item: GameItem):
        # add item to inventory if it is interactable, else tell player not interactable
        self.item = item
        if self.item.isInteractable and self.item in PlayerInstance.player.location.items:
            #update game state based on interaction
            if self.item.item_type == ItemType.artifact:
                state.active_flags.add(GameFlag.found_artifact)
            elif self.item.item_type == ItemType.journal:
                state.active_flags.add(GameFlag.found_journal)
            elif self.item.item_type == ItemType.sapphire_bracelet:
                state.active_flags.add(GameFlag.found_bracelet)
            elif self.item.item_type == ItemType.shrine:
                state.active_flags.add(GameFlag.found_shrine)
            elif self.item.item_type == ItemType.knife:
                state.active_flags.add(GameFlag.found_knife)
            PlayerInstance.player.inventory.append(self.item)
            PlayerInstance.player.location.items.remove(self.item)
        else:
            return "You cannot pick up this item or the item does not exist."
        return f'You pick up the {item}.'
    def drop(self, item: GameItem):
        self.item = item
        if self.item in PlayerInstance.player.inventory:
            PlayerInstance.player.inventory.remove(item)
            PlayerInstance.player.location.items.append(item)
            return f'You drop the {self.item.name}.'
        else:
            return "You do not have that item"
    def inspect(self, thing):
        return getattr(thing, 'description', 'There is nothing special about it.')

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
                return self.commands.navigate(self.location)
            else:
                return "That location does not exist."
        #--system commands
        elif self.cmd.startswith('inventory'):
            return self.commands.inventory(PlayerInstance.player.inventory)
        elif self.cmd.startswith('help'):
            return self.commands.info()
        #--item interaction--
        elif self.cmd.startswith('pick up'):
            item_name = self.cmd[7:].strip().lower()
            item = GameItem.get_by_name(self.item_name)
            if item:
                return self.commands.pick_up(item)
            else:
                return "That item does not exist."
        elif self.cmd.startswith('drop'):
            item_name = self.cmd[4:].strip().lower()
            item = GameItem.get_by_name(item_name)
            if item:
                return self.commands.drop(item)
            else:
                return "You do not have that item."
        elif self.cmd.startswith('inspect'):
            input_name = self.cmd[7:].strip().lower()
            inventory_items = PlayerInstance.player.inventory
            location_items = PlayerInstance.player.location.items
            #loops through inventory items, if none found loops location items, if none found checks  current location valid
            for item in inventory_items:
                if input_name == item.name.lower():
                    return self.commands.inspect(item)

            else:
                for item in location_items:
                    if input_name == item.name.lower():
                        return self.commands.inspect(item)
                else:
                    if PlayerInstance.player.location.name.lower() == input_name:
                        return self.commands.inspect(PlayerInstance.player.location)
                    else:
                        return "There's nothing like that to inspect."

        #--npc interaction--
        elif self.cmd.startswith('talk to'):
            npc_name = self.cmd[7:].strip().lower()
            npc = NPC.get_by_name(npc_name)
            if npc and npc in PlayerInstance.player.location.npcs:
                return self.commands.talk(npc)
            else:
                return f"{npc.get_by_name} is not in your location."
            
        elif self.cmd.startswith('ask'):
            #remove prefix, then split the command to access the elements
            input_str = self.cmd[4:].strip().lower()
            if ' about ' in input_str:
                npc_name, topic = input_str.split(' about ', 1)
                npc_name = npc_name.strip().lower()
                topic = topic.strip().lower()
                npc = NPC.get_by_name(npc_name)

                if npc and npc in PlayerInstance.player.location.npcs:
                    return self.commands.ask_about(npc, topic)
                else:
                    return f"{npc_name.capitalize()} doesn't have anything to say about the {topic}."
            else:
                return "Please format your question 'ask [name] about [topic]"
        else:
            return "Command not recognized. Type 'info' for help"