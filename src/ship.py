import pygame
from pathlib import Path

class Ship : 
    """A class to manage the Ship """
    
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position. """
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        #? Multiplatform Images
        curren_directory = Path(__file__).parent
        #? Build the complete route of the image
        image_path = curren_directory / 'Images' / 'ship.bmp'
        #? Load the ship image and get is rect 
        self.image = pygame.image.load(str(image_path))
        
        self.rect = self.image.get_rect()
        
        #? Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        #?Store a float for the ship's exact horizontal position
        self.x = float(self.rect.x)

        #?Movement flag; start with a ship tha's not moving.
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        """Update the ship's position based on the movement flag. """
        #?Update the ship's x value, not the rect

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        #?Update rect object from self.x
        self.rect.x = self.x

    def center_ship(self):
        """Center the ship on the screen. """
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)


    def blitme(self):
        """Draw the ship at its current location. """
        self.screen.blit(self.image, self.rect)
