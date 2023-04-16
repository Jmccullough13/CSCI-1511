import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """A class to manage the ship"""
    def __init__(self, ai_game):
        """Initialize the ship and set it's starting point"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #Load the ship image and get its rect
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        #Start each new ship at the right of the screen
        self.rect.midright = self.screen_rect.midright
        #Store a decimal value for the ship's horizontal position
        self.y = float(self.rect.y)
        # Movement flag.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on movement flags."""
        # Update the ship's x value, not the rect.
        if self.moving_right and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        if self.moving_left and self.rect.top > 0:
            self.y -= self.settings.ship_speed

        # Update rect object from self.y.
        self.rect.y = self.y

    def center_ship(self):
        """Center the ship on the screen"""
        self.rect.midright = self.screen_rect.midright
        self.y = float(self.rect.y)

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

