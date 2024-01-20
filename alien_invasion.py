import sys
import pygame
from settings import Setting
from ship import Ship

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.obj=Setting()
        self.screen=pygame.display.set_mode((self.obj.width, self.obj.height))
        pygame.display.set_caption('Alien Invasion')
        self.ship=Ship(self)
        
    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            
    def _check_events(self):
        for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()  
                elif event.type==pygame.KEYDOWN:
                    self. _key_down_controller(event)
                elif event.type==pygame.KEYUP:
                    self._key_up_controller(event)
                    
    def _key_down_controller(self, event):
        if event.key==pygame.K_RIGHT:    
                self.ship.right=True
        elif event.key==pygame.K_LEFT:
                self.ship.left=True
        elif event.key==pygame.K_UP:
                self.ship.up=True
        elif event.key==pygame.K_DOWN:
                self.ship.down=True
                
    def _key_up_controller(self, event):
        if event.key==pygame.K_RIGHT:
            self.ship.right=False
        elif event.key==pygame.K_LEFT:
            self.ship.left=False
        elif event.key==pygame.K_UP:
            self.ship.up=False
        elif event.key==pygame.K_DOWN:
            self.ship.down=False
            
    def _update_screen(self):
        self.screen.fill(self.obj.bg_color)
        self.ship.blitme()
        pygame.display.flip()
        
if __name__=='__main__':
    ai=AlienInvasion()
    ai.run_game()