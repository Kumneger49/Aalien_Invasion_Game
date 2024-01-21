import pygame

class Ship:
    def __init__(self, ai):
        self.screen=ai.screen
        self.obj=ai.obj
        self.screen_rect=ai.screen.get_rect()
        self.image=pygame.image.load('C:\\Users\\User\\Desktop\\Python\\Alien_Invasion\\images\\Rocket-147466_1280-_1_.bmp')
        self.image_rect=self.image.get_rect()
        self.image_rect.midbottom=self.screen_rect.midbottom
        self.x=float(self.image_rect.x)
        self.y=float(self.image_rect.y)
        self.right=False
        self.left=False
        self.up=False
        self.down=False
      
    def update(self):
        if self.right and self.image_rect.right<self.screen_rect.right:
            self.x+=self.obj.ship_speed
        if self.left and self.image_rect.left>0:
            self.x-=self.obj.ship_speed
        if self.up and self.image_rect.top>0:
            self.y-=self.obj.ship_speed
        if self.down and self.image_rect.bottom<self.screen_rect.bottom:
            self.y+=self.obj.ship_speed
        self.image_rect.x=self.x
        self.image_rect.y=self.y
        
    def blitme(self):
        self.screen.blit(self.image, self.image_rect)