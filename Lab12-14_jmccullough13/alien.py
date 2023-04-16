import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""
    def __init__(self, ai_game):
        """Initialize the alien sprite and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #load the image and set it's rect attributes
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #Start each new alien at the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store the alien's exact horizontal position
        self.y = float(self.rect.y)

    def check_edges(self):
        """Return true if the alien is at the edge if the screen"""
        screen_rect = self.screen.get_rect()
        return (self.rect.top >= 0) or (self.rect.bottom <= screen_rect.bottom)

    def update(self):
        """Move the alien to the right"""
        self.y += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.y = self.y


