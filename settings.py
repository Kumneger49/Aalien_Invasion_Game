class Setting: 
    def __init__(self):
        self.width=1200
        self.height=800
        self.bg_color=(0, 0, 0)
        self.ship_limit=3
        
        
        
        self.bullet_width=150
        self.bullet_height=15
        self.bullet_color=(255, 255, 0)
        self.bullets_allowed=10
        
        self.alien_bullet_width=30
        self.alien_bullet_height=20
        self.alien_bullet_color=(255, 0, 0)
        
        self.special_bullet_width=600
        self.special_bullet_height=15
        self.special_bullet_color=(255, 255, 255)
        
        
        self.aliens_drop_speed=8    
        self.rate=1.2
        self.score_up=2
        self.dynamic_setting()
        
    def dynamic_setting(self):
        self.alien_points=1
        self.alien_speed=1.5
        self.bullet_speed=12
        self.ship_speed=1.8
        self.fleet_direction=1
        self.alien_bullet_speed=0.3
        self.special_bullet_speed=14
    
    def speed_up(self):
        self.alien_speed*=self.rate
        self.bullet_speed*=self.rate
        self.alien_bullet_speed*=self.rate
        self.ship_speed*=self.rate
        self.alien_points=int(self.alien_points*self.score_up)