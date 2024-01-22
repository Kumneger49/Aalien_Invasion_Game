import pygame
from pygame.sprite import Sprite
 
class Alien(Sprite):
    def __init__(self, ai):
        super().__init__()
        self.var=0
        self.screen=ai.screen
        self.image=pygame.image.load("C:\\Users\\User\\Desktop\\Python\\Alien_Invasion\\images\\Toy-576514_1280-_2_.bmp")
        self.rect=self.image.get_rect()
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        self.x=float(self.rect.x)
        self.settings=ai.obj
    
    def check_edges(self):
        screen_rect=self.screen.get_rect()
        if self.rect.right>=screen_rect.right or self.rect.left<=0:
            return True
    
    def update(self):
        self.x+=self.settings.alien_speed*self.settings.fleet_direction
        self.rect.x=self.x