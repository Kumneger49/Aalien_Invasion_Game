import sys
import pygame
from settings import Setting
class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.obj=Setting()
        self.screen=pygame.display.set_mode((self.obj.width, self.obj.height))
        pygame.display.set_caption('Alien Invasion')
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.obj.bg_color)
            pygame.display.flip()
if __name__=='__main__':
    ai=AlienInvasion()
    ai.run_game()