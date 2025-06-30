import pygame
from interaction_handler import *
from game_state import *

class main:
    def __init__(self):
            pygame.init()

            self.WINDOW_WIDTH = 600
            self.WINDOW_HEIGHT = 600

            self.display_surface = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
            pygame.display.set_caption("Beneath Her Song")

            self.DARK_GREEN = (10, 50, 10)
            self.BLACK = (0, 0, 0)

            self.system_font = pygame.font.SysFont('calibri', 32)

    def render_text(self, text: str):
         pass

    #--main loop--
    def run(self):
        self.running = True
        while self.running == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Commands.quit_game()
                    self.running = False
                    return
        # display intro to player
        if not GameFlag.game_intro in state.active_flags:
             intro_text = ""
             commands = Commands.info()
             main.render_text(intro_text)
             main.render_text("Commands: " + commands)
        # prompt & wait for user input

main().run()