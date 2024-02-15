import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, ai):
        super().__init__()
        self.screen=ai.screen
        self.obj=ai.obj
        self.screen_rect=ai.screen.get_rect()
        self.image=pygame.image.load('images\\Rocket-147466_1280-_1_.bmp')
        self.rect=self.image.get_rect()
        self.rect.midbottom=self.screen_rect.midbottom
        self.x=float(self.rect.x)
        self.y=float(self.rect.y)
        self.right=False
        self.left=False
        self.up=False
        self.down=False
      
    def update(self):
        if self.right and self.rect.right<self.screen_rect.right:
            self.x+=self.obj.ship_speed
        if self.left and self.rect.left>0:
            self.x-=self.obj.ship_speed
        if self.up and self.rect.top>0:
            self.y-=self.obj.ship_speed
        if self.down and self.rect.bottom<self.screen_rect.bottom:
            self.y+=self.obj.ship_speed
        self.rect.x=self.x
        self.rect.y=self.y
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)
        
    def center_ship(self):
        self.rect.midbottom=self.screen_rect.midbottom
         
