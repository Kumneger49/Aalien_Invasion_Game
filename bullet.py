import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai):
        super().__init__()
        self.screen=ai.screen
        self.settings=ai.obj
        self.color=ai.obj.bullet_color
        self.rect=pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop=ai.ship.rect.midtop
        self.y=float(self.rect.y)
        
    def update(self):
        self.y-=self.settings.bullet_speed
        self.rect.y=self.y
    
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        
class AlienBullet(Sprite):
    def __init__(self, ai):
        super().__init__()
        self.ai=ai
        self.screen=ai.screen
        self.settings=ai.obj
        self.color=ai.obj.alien_bullet_color
        self.rect=pygame.Rect(0,0, self.settings.alien_bullet_width, self.settings.alien_bullet_height)
        self._pos()
        self.y=float(self.rect.y)

    def _pos(self):
        for alien in self.ai.aliens:
            self.rect.midtop=alien.rect.midbottom

    def update(self):
        self.y+=self.settings.alien_bullet_speed
        self.rect.y=self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

        
class SpeciaBullet(Sprite):
    def __init__(self, ai):
        super().__init__()
        self.settings=ai.obj
        self.screen=ai.screen
        self.color=ai.obj.special_bullet_color
        self.rect=pygame.Rect(0,0, self.settings.special_bullet_width, self.settings.special_bullet_height)
        self.rect.midtop=ai.ship.rect.midtop
        self.y=float(self.rect.y)
        
    def update(self):
        self.y-=self.settings.special_bullet_speed
        self.rect.y=self.y
    
    def draw_special_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect) 