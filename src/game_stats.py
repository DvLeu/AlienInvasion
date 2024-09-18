class GameStats:
    """Tack stattistics for Alien Invasion"""

    def __init__(self, ai_game):
        """Initialize stattistics. """
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics"""
        self.ships_left = self.settings.ship_limit
