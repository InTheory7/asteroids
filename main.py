import pygame
import sys
from constants import * # Or `from constants import *`
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    # Initialize pygame modules:
    pygame.init()
    # Print CLI starting messages:
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Create the GUI window:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Create the clock:
    clock = pygame.time.Clock()
    dt = 0      # Delta time, needs to be predefined for its first use

    # Create two groups for updatable and drawable obecjts:
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # Add the Player class to both groups:
    Player.containers = (updatable, drawable)

    # Create a group for the asteroids:
    asteroids = pygame.sprite.Group()

    # Add the containers field of the Asteroid class to the asteroids,
        # updatable, and drawable groups:
    Asteroid.containers = (asteroids, updatable, drawable)

    # Add AsteroidField class to the updatable group:
    AsteroidField.containers = updatable

    # Create a group for the shots:
    shots = pygame.sprite.Group()

    # Add the Shot class to the shots group:
    Shot.containers = (shots, updatable, drawable)

    # Create a player object:
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x,y)

    # Create the asteroid field:
    asteroidfield = AsteroidField()
    
    # Game Loop
    while True:
        # Exit the game if the GUI window is closed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Fill the screen with black (takes a tuple of RGB
            # values), i.e. clear the screen and set a background:
        screen.fill((0,0,0))

        # Iterate over all updatables and update them:
        for updatable_obj in updatable:
            updatable_obj.update(dt)

        # Iterate over all drawables and draw them:
        for drawable_obj in drawable:
            drawable_obj.draw(screen)

        pygame.display.flip()   # Update the screen

        # Hold each frame until 1/60th of a second has passed:
        dt = clock.tick(60)/1000 # Return delta time in seconds

        # For each asteroid in the frame...
        for asteroid in asteroids:
            # Check if they collide with the player...
            if asteroid.collision(player):
                # If they do, exit the game:
                print("Game over!")
                sys.exit()
            # Check if they collide with any shots...
            for shot in shots:
                # Loop over each shot and check collision:
                if asteroid.collision(shot):
                    # If they collide, destroy both:
                    asteroid.split()
                    shot.kill()


if __name__ == "__main__":
    main()