class Setting: 
    def __init__(self):
        self.width=1200
        self.height=800
        self.bg_color=(0, 0, 0)
        self.ship_speed=1.8
        self.ship_limit=3
        
        self.bullet_speed=12
        self.bullet_width=150
        self.bullet_height=15
        self.bullet_color=(255, 255, 0)
        self.bullets_allowed=10
        
        self.alien_speed=4.3
        self.aliens_drop_speed=20
        self.fleet_direction=1