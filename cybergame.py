import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BG_COLOR = (255, 255, 255)  # White
TEXT_COLOR = (0, 0, 0)      # Black
BUTTON_COLOR = (0, 100, 0)  # Dark Green
BUTTON_TEXT_COLOR = (255, 255, 255)  # White

# Create the Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cyber Awareness Game")

# Load fonts
font = pygame.font.Font(None, 36)

# Create a "Get Started" button
button_rect = pygame.Rect(300, 400, 200, 50)
button_text = font.render("Get Started", True, BUTTON_TEXT_COLOR)
button_text_rect = button_text.get_rect(center=button_rect.center)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                print("Get Started button clicked!")  # You can add your logic here

    # Clear the screen
    screen.fill(BG_COLOR)

    # Display the welcome message
    welcome_text = font.render("Welcome to the Cyber Awareness Game", True, TEXT_COLOR)
    welcome_text_rect = welcome_text.get_rect(center=(WIDTH // 2, 200))
    screen.blit(welcome_text, welcome_text_rect)

    # Draw the "Get Started" button with dark green color
    pygame.draw.rect(screen, BUTTON_COLOR, button_rect)
    screen.blit(button_text, button_text_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()


