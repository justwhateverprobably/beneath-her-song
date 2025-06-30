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
         #auto scroll
         #text bounds
         pass

    #--main loop--
    def run(self):
        self.running = True
        while self.running == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.running = False
                    return
        # display intro to player
        if not GameFlag.game_intro in state.active_flags:
             intro_text = """
                The town's smaller than you expected. Quiet. People keep to themselves.
                You've been staying up at the lighthouse — it's cold, but it's dry, and the lamp keeps you busy at night.
                When the fog isn't too thick, you can see the tavern down the hill. A few familiar faces come and go. No one says much unless they've had a drink or two.
                Closer to the water, the docks are always shifting — boards groaning, ropes straining. Some of the boats haven't moved in a long time.
                There's a narrow path behind the tavern that winds into the forest. You haven't gone far. The trees feel like they're listening.
                And the beach… the beach is always quiet, but never still. Something about it makes you uneasy, though you can't say why.
                It's not a bad place.  
                Just... a strange one.  
                You're still settling in though.
                Maybe it just takes time to get used to.
                """
             main.render_text(intro_text)
             main.render_text("Type 'help' for a list of commands.")
             state.active_flags.add(GameFlag.game_intro)
        # prompt & wait for user input
        player_input = print(input("> "))

main().run()