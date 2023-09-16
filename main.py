import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants for screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Title")

# Game font
font = pygame.font.Font(None, 36)

# Intro screen text
intro_text = "Welcome"
start_text = "Press SPACE to Start"

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            running = False  # Exit the intro screen if SPACE is pressed

    # Clear the screen
    screen.fill(WHITE)

    # Render text
    intro_render = font.render(intro_text, True, BLACK)
    start_render = font.render(start_text, True, GREEN)

    # Blit text to the screen
    screen.blit(intro_render, (SCREEN_WIDTH // 2 - intro_render.get_width() // 2, 200))
    screen.blit(start_render, (SCREEN_WIDTH // 2 - start_render.get_width() // 2, 300))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()