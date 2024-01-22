import sys
from time import sleep
import pygame
from settings import Setting
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.a=0
        self.obj=Setting()
        self.screen=pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.obj.width = self.screen.get_rect().width
        self.obj.height = self.screen.get_rect().height
        pygame.display.set_caption('Alien Invasion')
        self.stats=GameStats(self)
        self.ship=Ship(self)
        self.bullets=pygame.sprite.Group()
        self.aliens=pygame.sprite.Group()
        self._create_fleet()
        
    def run_game(self):
        while True:
            self._check_events()
            if self.stats.game_active==True:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()
            
    def _check_events(self):
        for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()  
                elif event.type==pygame.KEYDOWN:
                    self._key_down_controller(event)
                elif event.type==pygame.KEYUP:
                    self._key_up_controller(event)
 
    def _key_up_controller(self, event):
        if event.key==pygame.K_RIGHT:
            self.ship.right=False
        elif event.key==pygame.K_LEFT:
            self.ship.left=False
        elif event.key==pygame.K_UP:
            self.ship.up=False
        elif event.key==pygame.K_DOWN:
            self.ship.down=False
                    
    def _key_down_controller(self, event):
        if event.key==pygame.K_RIGHT:    
            self.ship.right=True
        elif event.key==pygame.K_LEFT:
            self.ship.left=True
        elif event.key==pygame.K_UP:
            self.ship.up=True
        elif event.key==pygame.K_DOWN:
            self.ship.down=True
        elif event.key==pygame.K_SPACE:
            self._fire_bullets()
        elif event.key==pygame.K_q:
            sys.exit()
    
    def _fire_bullets(self):
        if self.obj.bullets_allowed>len(self.bullets):
            self.bullet=Bullet(self)  
            self.bullets.add(self.bullet)
            
    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom<=0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()
        
    def _check_bullet_alien_collisions(self):
        collisions=pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if not self.aliens:
            self.bullets.empty()  
            self._create_fleet()  
    def _update_aliens(self):                  
        self._check_aliens() 
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        self._check_aliens_bottom()
        
    def _check_aliens(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
            
    def _ship_hit(self):
        if self.stats.ships_left>0:
            self.stats.ships_left-=1
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self.ship.center_ship()
        else:
            self.stats.game_active=False
            self.ship.center_ship()
        
    def _check_aliens_bottom(self):
        screen_rect=self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom>=screen_rect.bottom:
                self._ship_hit()
                break
            
    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y+=self.obj.aliens_drop_speed
        self.obj.fleet_direction*=-1
    
    def _create_fleet(self):
        alien=Alien(self)
        alien_width, alien_height=alien.rect.size
        available_space_x=self.obj.width-(2*alien_width)   
        number_aliens_x=available_space_x//(2*alien_width)
        ship_height=self.ship.rect.height
        available_space_y=(self.obj.height-(3*alien_height)-ship_height)
        rows=available_space_y//(2*alien_height)
        for row in range(rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row)
            
    def _create_alien(self, alien_number, row):
        alien=Alien(self)
        alien_width=alien.rect.width
        alien.x=alien_width + 2*alien_width*alien_number
        alien.rect.x=alien.x
        alien.rect.y=alien.rect.height+2*alien.rect.height*row
        self.aliens.add(alien)
            
    def _update_screen(self):
        self.screen.fill(self.obj.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        pygame.display.flip()
        
if __name__=='__main__':
    ai=AlienInvasion()
    ai.run_game()
    