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
        print(inventory)
    def info():
        commands = ['quit', 'inventory', 'go to [location]', 'pick up [item]', 'drop [item]', 'use [item]', 'inspect [item/location]', 'talk to [name]', 'ask [name] about [topic]']
        print(commands)
    #--navigation--
    def navigate(location: GameLocation):
        PlayerInstance.player.location = location
    #--npc interaction--
    def talk(npc: NPC):
        line = DialogueHandler.talk_to(npc.name)
        if npc in PlayerInstance.player.location.npcs:
            print(line)
        else:
            print(f"{npc.get_by_name} is not in your location.")
    def ask_about(npc: NPC, topic):
        line = DialogueHandler.ask_about(npc.name, topic)
        if npc in PlayerInstance.player.location.npcs:
            print(line)
        else:
            print(f"{npc.get_by_name} is not in your location.")
    #--item interaction--
    def pick_up(item: GameItem):
        # add item to inventory if it is interactable, else tell player not interactable
        if item.isInteractable:
            PlayerInstance.player.inventory.append(item)
            PlayerInstance.player.location.items.remove(item)
        else:
            print("You cannot pick up this item")
            return
        #update game state based on interaction
        if item.item_type == ItemType.artifact:
            state.active_flags.add(GameFlag.found_artifact)
        elif item.item_type == ItemType.journal:
            state.active_flags.add(GameFlag.found_journal)
        elif item.item_type == ItemType.sapphire_bracelet:
            state.active_flags.add(GameFlag.found_bracelet)
        elif item.item_type == ItemType.shrine:
            state.active_flags.add(GameFlag.found_shrine)
        else:
            pass
        print(f'You pick up the {item}.')
    def drop(item: GameItem):
        if item in PlayerInstance.player.inventory:
            PlayerInstance.player.inventory.remove(item)
            PlayerInstance.player.location.items.append(item)
            print(f'You drop the {item}.')
        else:
            print("You do not have that item")
    def inspect(item):
        print(item.description)

class CommandHandler:
    def handle_command(self, command):
        self.cmd = command.strip().lower()

        #--navigation
        if self.cmd.startswith('go to'):
            location = self.cmd[6:]
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
            item = self.cmd[7:]
            Commands.pick_up(item)
        elif self.cmd.startswith('drop'):
            item = self.cmd[4:]
            Commands.drop(item)
        elif self.cmd.startswith('use'):
            item = self.cmd[3:]
            Commands.use(item)
        elif self.cmd.startswith('inspect'):
            item = self.cmd[7:]
            Commands.inspect(item)
        #--npc interaction--
        elif self.cmd.startswith('talk to'):
            npc_name = self.cmd[7:]
            player = PlayerInstance.player
            valid_npcs = player.location.npcs
            npc = NPC.get_by_name(npc_name)
            if npc in valid_npcs:
                Commands.talk(npc)
            else:
                print(f"There is no one named {npc_name} here.")
        elif self.cmd.startswith('ask'):
            pass
        else:
            print('Command not recognized. Type "info" for help')