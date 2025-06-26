from npc import *
from items import GameItem
from locations import GameLocation
from player import *
from game_state import *
import pygame

class Commands:
    def quit_game():
        pygame.quit()
    def inventory(items: list[GameItem]):
        inventory = items
        print(inventory)
    def info():
        commands = ['quit', 'inventory', 'go to [location]', 'pick up [item]', 'drop [item]', 'use [item]', 'inspect [item/location]']
        print(commands)
    #--navigation--
    def navigate(location: GameLocation):
        PlayerInstance.player.location = location
    #--npc interaction--
    def talk(npc):
        #npc_dialogue = 
        #print(npc_dialogue)
        pass
    #--item interaction--
    def pick_up(item: GameItem):
        PlayerInstance.player.inventory.append(item)
        PlayerInstance.player.location.items.remove(item)
        if item.item_type == ItemType.artifact:
            GameState.active_flags.add(GameFlag.found_artifact)
        elif item.item_type == ItemType.coins:
            pass
        elif item.item_type == ItemType.journal:
            pass
        elif item.item_type == ItemType.knife:
            pass
        elif item.item_type == ItemType.sapphire_bracelet:
            pass
        elif item.item_type == ItemType.shrine:
            pass
        print(f'You pick up the {item}.')
    def drop(item: GameItem):
        PlayerInstance.player.inventory.remove(item)
        PlayerInstance.player.location.items.append(item)
        print(f'You drop the {item}.')
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
        else:
            print('Command not recognized. Type "info" for help')

class DialogueHandler:
    def handle_dialogue():
        npcs = NPC.all_npcs

        for npc in npcs:
            #get dialogues
            pass
        
        #print correspongding dialogue
        if NPC.npc_type() == NPCType.bartender:
            pass
        if NPC.npc_type() == NPCType.siren:
            pass
        if NPC.npc_type() == NPCType.sailor:
            pass
        if NPC.npc_type() == NPCType.marla:
            pass
        if NPC.npc_type() == NPCType.hermit:
            pass