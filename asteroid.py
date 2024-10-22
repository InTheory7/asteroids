import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        # (screen, colour, centre, linewidth)
        pygame.draw.circle(screen,"white",self.position,self.radius,2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        # Always kill the current asteroid:
        self.kill()
        # If the radius is <= min radius, just return:
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        # Define a random angle between 20 and 50 degrees:
        launch_angle = random.uniform(20,50)
        # Adjust the velocities by +- this angle:
        clockwise_velocity = self.velocity.rotate(launch_angle)
        anticlockwise_velocity = self.velocity.rotate(-launch_angle)
        # Calculate the new asteroid radii:
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        # Create the new asteroids:
        clockwise_asteroid = Asteroid(self.position[0], self.position[1], new_radius)
        anticlockwise_asteroid = Asteroid(self.position[0], self.position[1], new_radius)
        # Assign these asteroids with the new velocities and make them faster:
        clockwise_asteroid.velocity = clockwise_velocity * 1.2
        anticlockwise_asteroid.velocity = anticlockwise_velocity * 1.2