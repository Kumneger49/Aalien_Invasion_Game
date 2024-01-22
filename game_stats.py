
class GameStats:
    def __init__(self, ai):
        self.settings=ai.obj
        self.reset_stats()
        self.game_active=False
        
    def reset_stats(self):
        self.ships_left=self.settings.ship_limit