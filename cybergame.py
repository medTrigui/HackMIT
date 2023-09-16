import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1200, 750
BG_COLOR = (46, 49, 49)        # Dark Gray
TEXT_COLOR = (255, 255, 255)   # White
BUTTON_COLOR = (52, 152, 219)  # Blue
BUTTON_TEXT_COLOR = (255, 255, 255)  # White
BUTTON_BORDER_COLOR = (44, 62, 80)  # Dark Blue
BUTTON_HOVER_COLOR = (41, 128, 185)  # Light Blue
BUTTON_HOVER_TEXT_COLOR = (255, 255, 255)  # White
BUTTON_WIDTH, BUTTON_HEIGHT = 200, 50
BUTTON_RADIUS = 10
SMALL_BUTTON_WIDTH, SMALL_BUTTON_HEIGHT = 50, 30

# Create the Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cyber Awareness Game")

# Load fonts
font_title = pygame.font.Font(None, 56)  # Use the default font ("Courier")
font_button = pygame.font.Font(None, 36)
font_small_button = pygame.font.Font(None, 18)

# Input username
input_rect = pygame.Rect((WIDTH - BUTTON_WIDTH) // 2, 400, BUTTON_WIDTH, BUTTON_HEIGHT)
username = ""
username_active = False
username_color = BUTTON_BORDER_COLOR

# Create a "Start Game" button
start_button_rect = pygame.Rect((WIDTH - BUTTON_WIDTH) // 2, 270, BUTTON_WIDTH, BUTTON_HEIGHT)

# Create a "Back to Menu" button for Level 1
back_to_menu_button_rect = pygame.Rect(10, 10, SMALL_BUTTON_WIDTH, SMALL_BUTTON_HEIGHT)
back_to_menu_color = BUTTON_COLOR
back_to_menu_text_color = BUTTON_TEXT_COLOR

# Username placeholder text
placeholder_text = "Enter your username"
placeholder_font = pygame.font.Font(None, )  # You can adjust the font size

# Game state
game_state = "menu"  # Initial state is the menu

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if start_button_rect.collidepoint(event.pos):
                if username:  # Check if a username is entered
                    if game_state == "menu":
                        print(f"Start Game button clicked! Username: {username}")
                        # You can add your game logic here, passing the username to the game
                        # Switch to the game state
                        game_state = "level1"
                    elif game_state == "level1":
                        # Implement actions for level 1 here
                        pass
            elif input_rect.collidepoint(event.pos):
                username_active = not username_active
                username_color = BUTTON_COLOR if username_active else BUTTON_BORDER_COLOR
        
        elif game_state == "level1" and back_to_menu_button_rect.collidepoint(event.pos):
                # Handle clicking the "Back to Menu" button in Level 1
                game_state = "menu"
        
        elif event.type == pygame.KEYDOWN:
            if username_active:
                if event.key == pygame.K_RETURN:
                    username_active = False
                    username_color = BUTTON_BORDER_COLOR
                elif event.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                else:
                    username += event.unicode

    # Clear the screen
    screen.fill(BG_COLOR)

    if game_state == "menu":
        # Display the welcome message
        welcome_text = font_title.render("SecurEscape: The Cyber Chronicles", True, TEXT_COLOR)
        welcome_text_rect = welcome_text.get_rect(center=(WIDTH // 2, 150))
        screen.blit(welcome_text, welcome_text_rect)

        # Draw the username input box with a distinct color
        pygame.draw.rect(screen, username_color, input_rect, border_radius=BUTTON_RADIUS)
        if username_active:
            pygame.draw.rect(screen, BUTTON_HOVER_COLOR, input_rect, border_radius=BUTTON_RADIUS)

        # Draw the username text inside the input box as you enter it
        username_text = font_button.render(username, True, BUTTON_TEXT_COLOR)

        # Adjust the y-coordinate of the text rect to position it higher
        username_text_rect = username_text.get_rect(center=(input_rect.centerx, input_rect.centery - 10))

        screen.blit(username_text, username_text_rect)

        # Draw the "Start Game" button with rounded corners
        pygame.draw.rect(screen, BUTTON_BORDER_COLOR, start_button_rect)
        pygame.draw.rect(screen, BUTTON_COLOR, start_button_rect, border_radius=BUTTON_RADIUS)

        # Check if the mouse is over the button and change colors accordingly
        if start_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, BUTTON_HOVER_COLOR, start_button_rect, border_radius=BUTTON_RADIUS)
            start_button_text = font_button.render("Start Game", True, BUTTON_HOVER_TEXT_COLOR)
        else:
            start_button_text = font_button.render("Start Game", True, BUTTON_TEXT_COLOR)

        start_button_text_rect = start_button_text.get_rect(center=start_button_rect.center)
        screen.blit(start_button_text, start_button_text_rect)

        # Display the username placeholder text if no username is entered
        if not username and not username_active:
            placeholder_render = placeholder_font.render(placeholder_text, True, BUTTON_BORDER_COLOR)
            placeholder_rect = placeholder_render.get_rect(center=input_rect.center)
            screen.blit(placeholder_render, placeholder_rect)

    elif game_state == "level1":
        # Display the level 1 message
        level1_text = font_button.render("Welcome to Level 1", True, TEXT_COLOR)
        level1_text_rect = level1_text.get_rect(center=(WIDTH // 2, 100))
        screen.blit(level1_text, level1_text_rect)

         # Draw the "Back to Menu" button in Level 1
        pygame.draw.rect(screen, back_to_menu_color, back_to_menu_button_rect, border_radius=BUTTON_RADIUS)
        back_to_menu_text = font_small_button.render("Menu", True, back_to_menu_text_color)
        back_to_menu_text_rect = back_to_menu_text.get_rect(center=back_to_menu_button_rect.center)
        screen.blit(back_to_menu_text, back_to_menu_text_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()