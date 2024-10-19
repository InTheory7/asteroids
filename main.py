import pygame
from constants import * # Or `from constants import *`

def main():
    # Initialize pygame modules:
    pygame.init()
    # Create the GUI window:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Game Loop
    while True:
        screen.fill((0,0,0))    # Fill the screen with black (takes a tuple of RGB values).
        pygame.display.flip()   # Update the screen

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()