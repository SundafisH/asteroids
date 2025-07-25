import pygame
from player import *
import math

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        points = [ (int(p.x), int(p.y)) for p in self.triangle() ]
        pygame.draw.polygon(screen, "white", points, 2)

    def update(self, dt):
        # sub-classes must override
        pass

    def collide(self, object):
        distance = self.position.distance_to(object.position)
        if distance <= self.radius + object.radius:
            return True
        else:
            return False

