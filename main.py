import pygame
from constants import * # Or `from constants import *`

def main():
    # Initialize pygame modules:
    pygame.init()
    # Print CLI starting messages:
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Create the GUI window:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Game Loop
    while True:
        # Exit the game if the GUI window is closed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0,0,0))    # Fill the screen with black (takes a tuple of RGB values).
        pygame.display.flip()   # Update the screen

if __name__ == "__main__":
    main()