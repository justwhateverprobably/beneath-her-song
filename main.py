import pygame
from interaction_handler import *
from game_state import *
from player import *

class Main:
    def __init__(self, width=600, height=800):
            pygame.init()
            self.width = width
            self.height = height
            self.bg_color = (0, 0, 0)
            self.surface = pygame.display.set_mode((self.width, self.height))
            self.renderer = Renderer(self.surface, self.width, self.height)
            self.input_handler = InputHandler()
            self.awaiting_restart = False

    def render_input(self):
        self.renderer.update(None, self.player_input)
    def render_feedback(self, text):
        self.renderer.update(text, self.player_input)
    
    #--main loop--
    def run(self):
        self.player_input = ""

        # display intro to player
        if not GameFlag.game_intro in state.active_flags:
            self.display_intro_screen()
            
        self.running = True
        while self.running:
            if not self.awaiting_restart:
                if GameFlag.won_game in state.active_flags:
                    win_text = "The fog finally lifts, and with it, the weight that has hung over this place. The sea's song fades into a gentle whisper, and the lighthouse lamp burns steady through the night. You've faced the shadows, calmed the restless spirits, and the town breathes again. Though the night is quiet now, you know the sea will always sing — but this time, it's a song of peace."
                    self.render_feedback(win_text)
                    self.display_end_screen()
                elif GameFlag.lost_game in state.active_flags:
                    lose_text = "The cold seeps in deeper than you expected, and the shadows claw into your head. The sound of the waves swallow your cries for help, and the darkness feels like it's closing in from every side. No one will find you here. The voice of the siren lures you in closer… closer. The town moves on — but you're gone, just another story swallowed by the tides."
                    self.render_feedback(lose_text)
                    self.display_end_screen()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.running = False
                    return
                if event.type == pygame.KEYDOWN:
                    character = event.unicode
                    if event.key == pygame.K_RETURN:
                        playerInput = self.player_input.strip()

                        if playerInput:
                            if self.awaiting_restart:
                                if playerInput == 'y':
                                    self.restart_game()
                                    self.display_intro_screen()
                                    self.awaiting_restart = False
                                    state.active_flags.add(GameFlag.game_intro)
                                elif playerInput == 'n':
                                    self.running = False
                                    return
                                else:
                                    self.render_feedback("Please enter 'y' or 'n'.")
                                self.player_input = ''
                            else:
                                command_text = "> " + playerInput
                                response = None
                                response = self.input_handler.handle_command(playerInput)
                                self.render_feedback(command_text)
                                if response:
                                    self.render_feedback(response)
                                self.player_input = ""
                            
                    elif event.key == pygame.K_BACKSPACE:
                        self.player_input = self.player_input[:-1]
                    else:
                        self.player_input += character
            
            self.render_input()
    
    def display_intro_screen(self):
        intro_text = "The town's smaller than you expected. Quiet. People keep to themselves. You've been staying up at the lighthouse — it's cold, but it's dry, and the lamp keeps you busy at night. When the fog isn't too thick, you can see the tavern down the hill. A few familiar faces come and go. No one says much unless they've had a drink or two. Closer to the water, the docks are always shifting — boards groaning, ropes straining. Some of the boats haven't moved in a long time. There's a narrow path behind the tavern that winds into the forest. You haven't gone far. The trees feel like they're listening. And the beach… the beach is always quiet, but never still. Something about it makes you uneasy, though you can't say why. It's not a bad place. Just… a strange one. You're still settling in though. Maybe it just takes time to get used to."
        self.render_feedback(intro_text)
        self.render_feedback("Type 'help' for a list of commands.")
        state.active_flags.add(GameFlag.game_intro)

    def display_end_screen(self):
        state.active_flags.clear()
        self.awaiting_restart = True
        self.render_feedback("Would you like to play again? (y/n)")
    
    def restart_game(self):
        self.player_input = ''
        state.active_flags.clear()
        PlayerInstance.player.location = PlayerInstance.start_location
        PlayerInstance.player.inventory.clear()
        self.renderer.lines.clear()


class Renderer:
    def __init__(self, surface, width, height, font_size=18, line_spacing=5):
        self.surface = surface
        self.width = width
        self.height = height
        self.font_size = font_size
        self.line_spacing = line_spacing
        self.text_color = (10, 150, 10) #dark green
        self.bg_color = (0, 0, 0) #black
        self.lines = []

        self.system_font = pygame.font.SysFont('calibri', 18)
        pygame.display.set_caption("Beneath Her Song")


    def update(self, feedback_text: str, input_text: str):    
        if feedback_text:
            self.add_wrapped_text(feedback_text)
        
        x, y = 20, 20
        self.surface.fill(self.bg_color)
        line_height = self.system_font.get_height() + self.line_spacing
        max_lines = self.height // (self.system_font.get_height() + self.line_spacing) - 1 #-1 so you can see input line

        #display previous lines
        for line in self.lines:
            text_surface = self.system_font.render(line.strip(), True, self.text_color)
            self.surface.blit(text_surface, (x, y))
            y += line_height
        
        #display input on last line
        if input_text is None:
            input_text = ""
        input_surface = self.system_font.render("> " + input_text.strip() + " |", True, self.text_color)
        self.surface.blit(input_surface, (x, y))

        while len(self.lines) > max_lines:
            self.lines.pop(0)

        pygame.display.update()

    def add_wrapped_text(self, text: str):
        import re
        sentences = re.findall(r'.+?(?:[.?!]|$)', text)
        max_width = self.width - 40
        
        for sentence in sentences:
            words = sentence.strip().split(' ')
            line = ""
            for word in words:
                test_line = line + word + " "
                test_width = self.system_font.size(test_line)[0]
                    
                if test_width > max_width:
                    self.lines.append(line.strip())
                    line = word + " "
                else:
                    line = test_line
            if line.strip():
                self.lines.append(line.strip())

Main().run()