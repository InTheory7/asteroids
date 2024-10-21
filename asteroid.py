import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        # (screen, colour, centre, linewidth)
        pygame.draw.circle(screen,"white",self.position,2)

    def update(self, dt):
        self.position += self.velocity * dt