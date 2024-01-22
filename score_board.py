import pygame.font
from pygame.sprite import Group
from ship import Ship

class ScoreBoard:
    def __init__(self, ai):
        self.ai=ai
        self.screen=ai.screen
        self.screen_rect=self.screen.get_rect()
        self.settings=ai.obj
        self.stats=ai.stats
        self.text_color=(255,  255, 255)
        self.font=pygame.font.SysFont(None, 60)
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
        
    def prep_score(self):
        self.str=str(f'Aliens killed: {self.stats.score}')
        self.score_image=self.font.render(self.str, True, self.text_color, self.settings.bg_color)
        self.image_rect=self.score_image.get_rect()
        self.image_rect.right=self.screen_rect.right-20
        self.image_rect.top=20
        
    def prep_high_score(self):
        with open('highscore.txt', 'r+') as f:
            self.stats.high_score=f.read()
        # rounded_high_score=round(int(self.stats.high_score), -1)
        # self.stats.high_score="{:,}".format(rounded_high_score)
        self.str=str(f'High score: {self.stats.high_score}')
        self.image_high_score=self.font.render(self.str, True, self.text_color, self.settings.bg_color)
        self.high_score_image_rect=self.image_high_score.get_rect()
        self.high_score_image_rect.centerx=self.screen_rect.centerx
        self.high_score_image_rect.top=self.image_rect.top
        
    def check_high_score(self):
        if self.stats.score>int(self.stats.high_score):
            self.stats.high_score=self.stats.score
        with open('highscore.txt', 'r+') as f:
            f.write(str(self.stats.high_score))
        self.prep_high_score()
        
    def prep_level(self):
        self.str=str(f'Level: {self.stats.level}')
        self.level_image=self.font.render(self.str, True, self.text_color, self.settings.bg_color)
        self.level_image_rect=self.level_image.get_rect()
        self.level_image_rect.right=self.image_rect.right
        self.level_image_rect.top=self.image_rect.bottom+10
    
    def prep_ships(self):
        self.ships=Group()  
        for ship_number in range(self.stats.ships_left):
            ship=Ship(self.ai)
            ship.rect.x=10+ship.rect.width*ship_number
            ship.rect.y=10
            self.ships.add(ship)
            
    def show_score(self):
        self.screen.blit(self.score_image, self.image_rect)
        self.screen.blit(self.image_high_score, self.high_score_image_rect)
        self.screen.blit(self.level_image, self.level_image_rect)
        self.ships.draw(self.screen)
    