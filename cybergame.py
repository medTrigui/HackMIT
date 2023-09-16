import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BG_COLOR = (46, 49, 49)        # Dark Gray
TEXT_COLOR = (255, 255, 255)   # White
BUTTON_COLOR = (52, 152, 219)  # Blue
BUTTON_TEXT_COLOR = (255, 255, 255)  # White
BUTTON_BORDER_COLOR = (44, 62, 80)  # Dark Blue
BUTTON_HOVER_COLOR = (41, 128, 185)  # Light Blue
BUTTON_HOVER_TEXT_COLOR = (255, 255, 255)  # White
BUTTON_WIDTH, BUTTON_HEIGHT = 200, 50
BUTTON_RADIUS = 10

# Create the Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sophisticated Cyber Awareness Game")

# Load fonts
font = pygame.font.Font(None, 48)  # Replace "font.ttf" with your preferred font file path

# Create a "Get Started" button
button_rect = pygame.Rect((WIDTH - BUTTON_WIDTH) // 2, 400, BUTTON_WIDTH, BUTTON_HEIGHT)

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

    # Draw the "Get Started" button with rounded corners
    pygame.draw.rect(screen, BUTTON_BORDER_COLOR, button_rect)
    pygame.draw.rect(screen, BUTTON_COLOR, button_rect, border_radius=BUTTON_RADIUS)

    # Check if the mouse is over the button and change colors accordingly
    if button_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, BUTTON_HOVER_COLOR, button_rect, border_radius=BUTTON_RADIUS)
        button_text = font.render("Get Started", True, BUTTON_HOVER_TEXT_COLOR)
    else:
        button_text = font.render("Get Started", True, BUTTON_TEXT_COLOR)

    button_text_rect = button_text.get_rect(center=button_rect.center)
    screen.blit(button_text, button_text_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()