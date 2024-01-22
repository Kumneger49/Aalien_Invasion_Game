import pygame.font

class GameStats:
    def __init__(self, ai):
        self.settings=ai.obj
        self.screen=ai.screen
        self.screen_rect=self.screen.get_rect()
        self.reset_stats()
        self.game_active=False
        self.high_score=0
        # with open('highscore.txt', 'w') as f:
        #     f.write(str(self.high_score))
        self.text_color=(255, 255, 255)
        self.font=pygame.font.SysFont(None, 80)
        
    def reset_stats(self):
        self.ships_left=self.settings.ship_limit
        self.score=0
        self.level=1
   
        