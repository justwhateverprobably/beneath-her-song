import pygame
from interaction_handler import *
from game_state import *
import textwrap

class Main:
    def __init__(self, width=600, height=800):
            pygame.init()
            self.width = width
            self.height = height
            self.bg_color = (0, 0, 0)
            self.surface = pygame.display.set_mode((self.width, self.height))

    #--main loop--
    def run(self):
        renderer = Renderer(self.surface, self.width, self.height)

        # display intro to player
        if not GameFlag.game_intro in state.active_flags:
            intro_text = "The town's smaller than you expected. Quiet. People keep to themselves. You've been staying up at the lighthouse — it's cold, but it's dry, and the lamp keeps you busy at night. When the fog isn't too thick, you can see the tavern down the hill. A few familiar faces come and go. No one says much unless they've had a drink or two. Closer to the water, the docks are always shifting — boards groaning, ropes straining. Some of the boats haven't moved in a long time. There's a narrow path behind the tavern that winds into the forest. You haven't gone far. The trees feel like they're listening. And the beach… the beach is always quiet, but never still. Something about it makes you uneasy, though you can't say why. It's not a bad place. Just… a strange one. You're still settling in though. Maybe it just takes time to get used to."
            renderer.render_text(intro_text)
            renderer.render_text("Type 'help' for a list of commands.")
            state.active_flags.add(GameFlag.game_intro)
            
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.running = False
                    return
            # prompt & wait for user input
            #player_input = input("> ")

class Renderer:
    def __init__(self, surface, width, height, font_size=18, line_spacing=5):
        self.surface = surface
        self.width = width
        self.height = height
        self.font_size = font_size
        self.line_spacing = line_spacing
        self.text_color = (10, 150, 10) #dark green
        self.bg_color = (0, 0, 0) #black
        self.y_offset = 20

        self.system_font = pygame.font.SysFont('calibri', 18)
        pygame.display.set_caption("Beneath Her Song")

    def render_text(self, text: str):
            import re
            sentences = re.findall(r'[^.]*\.', text)
            x = 20
            max_width = self.width - 40

            #draw the first part of the sentence
            for sentence in sentences:
                words = sentence.strip().split(' ')
                line = ""
                for word in words:
                    test_line = line + word + " "
                    test_width = self.system_font.size(test_line)[0]
                      
                    if test_width > max_width:
                        text_surface = self.system_font.render(line.strip(), True, self.text_color)
                        self.surface.blit(text_surface, (x, self.y_offset))
                        self.y_offset += self.system_font.get_height() + self.line_spacing
                        line = word + " " #start new line with current word
                    else:
                        line = test_line # add the test line to the current line and loop again
                if line.strip(): #draw the last part of the sentence
                    text_surface = self.system_font.render(line.strip(), True, self.text_color)
                    self.surface.blit(text_surface, (x, self.y_offset))
                    self.y_offset += self.system_font.get_height() + self.line_spacing

            pygame.display.update()

Main().run()