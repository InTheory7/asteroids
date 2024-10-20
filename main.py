import pygame
from constants import * # Or `from constants import *`
from player import Player

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

    # Create a player object:
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x,y)
    
    # Game Loop
    while True:
        # Exit the game if the GUI window is closed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Fill the screen with black (takes a tuple of RGB
            # values), i.e. clear the screen and set a background:
        screen.fill((0,0,0))

        # Player control using the .update() method of the Player class:
        player.update(dt)

        # Re-render the player on the screen each frame:
        player.draw(screen)

        pygame.display.flip()   # Update the screen

        # Hold each frame until 1/60th of a second has passed:
        dt = clock.tick(60)/1000 # Return delta time in seconds

if __name__ == "__main__":
    main()