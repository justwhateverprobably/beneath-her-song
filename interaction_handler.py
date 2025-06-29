from npc import *
from items import GameItem
from locations import GameLocation
from player import *
from game_state import *
from dialogue_handler import *
import pygame

class Commands:
    def quit_game():
        pygame.quit()
    def inventory(items: list[GameItem]):
        inventory = items
        response = print(inventory)
        return response
    def info():
        commands = ['quit', 'inventory', 'go to [location]', 'pick up [item]', 'drop [item]', 'use [item]', 'inspect [item/location]', 'talk to [name]', 'ask [name] about [topic]']
        response = print(commands)
        return response
    #--navigation--
    def navigate(location: GameLocation):
        PlayerInstance.player.location = location
        response = print(f"You go to the {location.name}.")
        return response
    #--npc interaction--
    def talk(npc: NPCInterface):
        line = DialogueHandler.talk_to(npc.name)
        return line
    def ask_about(npc: NPCInterface, topic):
        line = DialogueHandler.ask_about(npc.name, topic)
        return line
    def attack(npc: NPCInterface):
        npc_name = npc.name
        if not npc.isFriendly and GameItem.get_by_name('knife') in PlayerInstance.player.inventory:
            response = print(f"You draw your knife from its sheath, and attack them viciously.")
            if npc.npc_type == NPCType.siren:
                state.active_flags.add(GameFlag.won_game)
            return response
        elif npc.isFriendly:
            response = print("You cannot attack a friend.")
            return response
        else:
            response = print("You attempt to attack them, but find you have no weapon. Without one, you don't stand a chance.")
            if npc.npc_type == NPCType.siren:
                state.active_flags.add(GameFlag.lost_game)
            return response
    #--item interaction--
    def pick_up(item: GameItem):
        # add item to inventory if it is interactable, else tell player not interactable
        if item.isInteractable and item in PlayerInstance.player.location.items:
            #update game state based on interaction
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
            else:
                pass
            PlayerInstance.player.inventory.append(item)
            PlayerInstance.player.location.items.remove(item)
        else:
            resoponse = print("You cannot pick up this item or the item does not exist.")
            return resoponse
        resoponse = print(f'You pick up the {item}.')
        return resoponse
    def drop(item: GameItem):
        if item in PlayerInstance.player.inventory:
            PlayerInstance.player.inventory.remove(item)
            PlayerInstance.player.location.items.append(item)
            print(f'You drop the {item}.')
        else:
            print("You do not have that item")
    def inspect(item):
        response = print(item.description)
        return response

class InputHandler:
    def handle_command(self, command):
        self.cmd = command.strip().lower()

        #--navigation
        if self.cmd.startswith('go to'):
            location_name = self.cmd[6:]
            location = GameLocation.get_by_name(location_name)
            Commands.navigate(location)
        #--system commands
        elif self.cmd.startswith('quit'):
            Commands.quit_game()
        elif self.cmd.startswith('inventory'):
            Commands.inventory()
        elif self.cmd.startswith('help'):
            Commands.info()
        #--item interaction--
        elif self.cmd.startswith('pick up'):
            item_name = self.cmd[7:]
            item = GameItem.get_by_name(item_name)
            Commands.pick_up(item)
        elif self.cmd.startswith('drop'):
            item_name = self.cmd[4:]
            item = GameItem.get_by_name(item_name)
            Commands.drop(item)
        elif self.cmd.startswith('use'):
            item_name = self.cmd[3:]
            item = GameItem.get_by_name(item_name)
            Commands.use(item)
        elif self.cmd.startswith('inspect'):
            item_name = self.cmd[7:]
            item = GameItem.get_by_name(item_name)
            Commands.inspect(item)
        #--npc interaction--
        elif self.cmd.startswith('talk to'):
            npc_name = self.cmd[7:]
            npc = NPC.get_by_name(npc_name)
            if npc and npc in PlayerInstance.player.location.npcs:
                response = Commands.talk(npc)
                print(response)
            else:
                print(f"{npc.get_by_name} is not in your location.")
            
        elif self.cmd.startswith('ask'):
            #remove prefix, then split the command to access the elements
            input_str = self.cmd[4:].strip()
            if ' about ' in input_str:
                npc_name, topic = input_str.split(' about ', 1)
                npc_name = npc_name.strip().lower()
                topic = topic.strip().lower()
                npc = NPC.get_by_name(npc_name)

                if npc and npc in PlayerInstance.player.location.npcs:
                    response = Commands.ask_about(npc, topic)
                    print(response)
                else:
                    print(f"{npc.get_by_name} is not in your location")
        else:
            print('Command not recognized. Type "info" for help')