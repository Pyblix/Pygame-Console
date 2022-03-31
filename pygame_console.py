import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame, pygame_textinput
pygame.init()
pygame.font.init()

class Console(pygame_textinput.TextInputVisualizer):
    def __init__(self, width, height, background_color = 'black', caption = 'console', text_font = 'arial', history_font = 'arial', prefix = '>', icon = None, text_color = 'white', cursor_color = 'white',
                 history_color = 'white', fps = 60, resizable = True):
        super(Console, self).__init__(cursor_color = cursor_color, font_color = text_color, font_object = pygame.font.SysFont(text_font, 30))
        self.background_color = background_color
        self.width = width
        self.height = height
        self.running = True
        self.fps = fps
        self.history = []
        self.caption = caption
        self.icon = icon
        self.font = pygame.font.SysFont(history_font, 20)
        self.history_color = history_color
        self.prefix = prefix
        self.resizable = resizable
        self.position = 0
    def draw_history(self):
        """Draws console history."""
        x = 10
        y = self.height - 2*self.surface.get_height()
        for c in self.history:
            self.screen.blit(self.font.render(c, True, self.history_color), (x, y + self.position))
            y -= 22
    def check_input(self, input):
        if input == 'help':
            return help(Console)
        else:
            return input
    def cprint(self, text = None):
        if text != None:
            self.value = text
        self.history.insert(0, f'{self.prefix} {self.check_input(self.value)}')
        self.value = ''
    def check_events(self):
        for event in self.events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.VIDEORESIZE:
                self.width = event.w
                self.height = event.h
                self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.cprint()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    self.position -= 10
                elif event.button == 5:
                   self.position += 10
    def redraw(self):
        self.screen.fill(self.background_color)
        self.draw_history()
        self.screen.blit(self.surface, (10, self.height - self.surface.get_height()-10))
        pygame.display.set_caption(self.caption)
        try:
            pygame.display.set_icon(self.icon)
        except:
            None
    def run(self):
        self.screen = pygame.display.set_mode((self.width, self.height)) if self.resizable == False else pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        while self.running:
            self.redraw()
            self.events = pygame.event.get()
            self.update(self.events)
            self.check_events()
            pygame.display.update()
            self.clock.tick(self.fps)
