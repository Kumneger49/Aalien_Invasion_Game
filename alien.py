import pygame
from pygame.sprite import Sprite
 
class Alien(Sprite):
    def __init__(self, ai):
        super().__init__()
        self.screen=ai.screen
        self.image=pygame.image.load("C:\\Users\\User\\Desktop\\Python\\Alien_Invasion\\images\\Toy-576514_1280-_2_.bmp")
        self.rect=self.image.get_rect()
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        self.x=float(self.rect.x)