import sys
from time import sleep
import pygame
from settings import Setting
from game_stats import GameStats
from score_board import ScoreBoard
from ship import Ship
from bullet import Bullet, AlienBullet, SpeciaBullet
from alien import Alien
from button import Button
from random import randint


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
        self.alien_bullets=pygame.sprite.Group()
        self.aliens=pygame.sprite.Group()
        self.special_bullets=pygame.sprite.Group()
        self._create_fleet()
        self.play_button=Button(self, 'Play')
        self.sb=ScoreBoard(self)
        
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
                elif event.type==pygame.MOUSEBUTTONDOWN:
                    mouse_pose=pygame.mouse.get_pos()
                    self._check_mouse_button(mouse_pose)
 
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
        elif event.key==pygame.K_p:
            self._start_game()
        elif event.key==pygame.K_q:
            sys.exit()
    
    def _fire_bullets(self):
        if self.obj.bullets_allowed>len(self.bullets):
            num=randint(0, 3)
            num_special=randint(0, 20)
            if num==0:
                alien_bullet=AlienBullet(self)
                self.alien_bullets.add(alien_bullet)
            if num_special==1:
                special_bullet=SpeciaBullet(self)
                self.special_bullets.add(special_bullet)
            else:
                bullet=Bullet(self)
                self.bullets.add(bullet)
    
    def _check_mouse_button(self, mouse_pose):
        button_clicked=self.play_button.rect.collidepoint(mouse_pose)
        if button_clicked and not self.stats.game_active:
            self._start_game()
            
    def _start_game(self):
            self.stats.reset_stats()
            self.stats.game_active=True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships() 
            self.bullets.empty()
            self.aliens.empty()
            self._create_fleet()
            self.ship.center_ship()
            pygame.mouse.set_visible(False)
            self.obj.dynamic_setting() 
                  
    def _update_bullets(self):
        self.bullets.update()
        self.alien_bullets.update()
        self.special_bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom<=0:
                self.bullets.remove(bullet)
        for special_bullet in self.special_bullets.copy():
            if special_bullet.rect.bottom<=0:
                self.special_bullets.remove(special_bullet)
        self._check_bullet_alien_collisions()
        
    def _check_bullet_alien_collisions(self):
        noraml_collisions=pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        special_bullet_collision=pygame.sprite.groupcollide(self.special_bullets, self.aliens, True, True)
        if noraml_collisions or special_bullet_collision:
            for aliens in noraml_collisions.values() or special_bullet_collision.values():
                self.stats.score+=self.obj.alien_points*len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
        if not self.aliens:
            self.bullets.empty()  
            self.alien_bullets.empty()
            self._create_fleet()  
            self.obj.speed_up()
            self.stats.level+=1
            self.sb.prep_level()
            
    def _check_alien_bullet_collision(self):
        collisions=pygame.sprite.spritecollideany(self.ship, self.alien_bullets)
        if collisions:
            sleep(0.5)
            self._ship_hit()
            
            
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
            self.sb.prep_ships()
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self.ship.center_ship()
            sleep(0.5)
            pygame.mouse.set_visible(True)
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
            
    def _alien_bullets(self):
       for alien_bullet in self.alien_bullets.sprites():
            alien_bullet.draw_bullet()
            self._check_alien_bullet_collision()
            
    def _update_screen(self):
        self.screen.fill(self.obj.bg_color)
        if not self.stats.game_active:
            self.play_button.draw_buttons()
        if self.stats.game_active:
            self.ship.blitme()
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            for special_bullet in self.special_bullets.sprites():
                special_bullet.draw_special_bullet()
            self._alien_bullets()
            self.aliens.draw(self.screen)
            self.sb.show_score()
        pygame.display.flip()
        
if __name__=='__main__':
    ai=AlienInvasion()
    ai.run_game()
    