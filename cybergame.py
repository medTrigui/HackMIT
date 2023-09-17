import pygame
import sys
import textwrap

# Initialize Pygame
pygame.init()

# Constants
SIZE = WIDTH, HEIGHT = 1366, 766
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
font_text = pygame.font.Font(None, 24)
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

# Create continue button #1
continue_button_rect = pygame.Rect(WIDTH - 140, HEIGHT - 60, 100, 30)   # Adjust dimensions and position

# Create "Option 1" and "Option 2" buttons
option1_button_rect = pygame.Rect((WIDTH - SMALL_BUTTON_WIDTH) // 2 - 100, 500, 100, 30)
option2_button_rect = pygame.Rect((WIDTH - SMALL_BUTTON_WIDTH) // 2 + 100, 500, 100, 30)

# Username placeholder text
placeholder_text = "Enter your username"
placeholder_font = pygame.font.Font(None, )  # You can adjust the font size

# Game state
game_state = "menu"  # Initial state is the menu

# Text typing effect

def blit_text(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

typing_effect_text = '''Introduction: In an era of constantly evolving cybersecurity threats, the digital landscape presents ever-increasing challenges. Every year, new and more sophisticated forms of malware emerge, putting individuals' personal information and digital security at risk. Whether it's safeguarding your passwords, staying vigilant against phishing attempts, protecting your data, or navigating the internet securely. The choices you make in your daily online life can have significant consequences. In this series, we embark on a journey to impart essential knowledge about password security, phishing awareness, data protection, and safe internet usage. Our aim is to engage and educate you in a fun and interactive manner, empowering you to navigate the digital realm with confidence. By arming yourself with these skills, you can effectively thwart cybercriminals' traps and safeguard your personal information in today's ever-evolving digital world.'''
typed_text = ""
text_speed = 35  # Adjust the speed by changing the delay (lower value for faster typing)
typing_index = 0
typing_timer = pygame.time.get_ticks()

# Main loop
running = True
line_index = 0
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
                        # Display the sentences with word wrapping
                        while True:

                            dt = clock.tick(FPS) / 1000

                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    quit()

                            screen.fill(pygame.Color('white'))
                            blit_text(screen, typing_effect_text, (20, 20), font)
                            pygame.display.update()
                        current_time = pygame.time.get_ticks()
                        if current_time - typing_timer > text_speed and typing_index < len(typing_effect_text):
                            typed_text += typing_effect_text[typing_index]
                            typing_index += 1
                            typing_timer = current_time

                            # Check if the typed text exceeds the screen width
                            if font_button.size(typed_text)[0] > WIDTH - 40:  # Adjust the padding as needed
                            # Move to the next line
                                typed_text += "\n"
                        level1_text = font_button.render(typed_text, True, TEXT_COLOR)
                        level1_text_rect = level1_text.get_rect(topleft=(20, 20))  # Adjust the position as needed
                        screen.blit(level1_text, level1_text_rect)
            elif input_rect.collidepoint(event.pos):
                username_active = not username_active
                username_color = BUTTON_COLOR if username_active else BUTTON_BORDER_COLOR
        
        elif game_state == "level1" and back_to_menu_button_rect.collidepoint(event.pos):
                # Handle clicking the "Back to Menu" button in Level 1
                game_state = "menu"
        elif game_state == "level1" and continue_button_rect.collidepoint(event.pos):
            # Handle clicking the "Continue" button in Level 1
            game_state = "level2"

        elif game_state == "level2":
            if option1_button_rect.collidepoint(event.pos):
                # Handle clicking "Option 1" to transition to Level 3
                game_state = "level2_1"
            elif option2_button_rect.collidepoint(event.pos):
                # Handle clicking "Option 2" to transition to Level 4
                game_state = "level2_2"
        
        
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
       
        # Display the level 1 message with a typing effect
        current_time = pygame.time.get_ticks()
        if current_time - typing_timer > text_speed and typing_index < len(typing_effect_text):
            typed_text += typing_effect_text[typing_index]
            typing_index += 1
            typing_timer = current_time

        level1_text = font_button.render(typed_text, True, TEXT_COLOR)
        level1_text_rect = level1_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(level1_text, level1_text_rect)
        # Check if the typed text exceeds the screen width
        if font_small_button.size(typed_lines[line_index][:typing_index])[0] > WIDTH - 40:
            line_index += 1  # Move to the next line

        if line_index < len(typed_lines) and typing_index == len(typed_lines[line_index]):
            # Start typing the next line
            line_index += 1
            typing_index = 0
         # Draw the "Back to Menu" button in Level 1
        pygame.draw.rect(screen, back_to_menu_color, back_to_menu_button_rect, border_radius=BUTTON_RADIUS)
        back_to_menu_text = font_small_button.render("Menu", True, back_to_menu_text_color)
        back_to_menu_text_rect = back_to_menu_text.get_rect(center=back_to_menu_button_rect.center)
        screen.blit(back_to_menu_text, back_to_menu_text_rect)

         # Draw the "Continue" button in Level 1
        pygame.draw.rect(screen, BUTTON_BORDER_COLOR, continue_button_rect)
        pygame.draw.rect(screen, BUTTON_COLOR, continue_button_rect, border_radius=BUTTON_RADIUS)

        if continue_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, BUTTON_HOVER_COLOR, continue_button_rect, border_radius=BUTTON_RADIUS)
            continue_button_text = font_small_button.render("Continue", True, BUTTON_HOVER_TEXT_COLOR)
        else:
            continue_button_text = font_small_button.render("Continue", True, BUTTON_TEXT_COLOR)

        continue_button_text_rect = continue_button_text.get_rect(center=continue_button_rect.center)
        screen.blit(continue_button_text, continue_button_text_rect)

    elif game_state == "level2":
        # Clear the screen
        screen.fill(BG_COLOR)
        
        current_time_level2 = pygame.time.get_ticks()
        if current_time_level2 - typing_timer_level2 > text_speed_level2 and typing_index_level2 < len(level2_text):
            typed_level2_text += level2_text[typing_index_level2]
            typing_index_level2 += 1
            typing_timer_level2 = current_time_level2

        level2_display_text = font_button.render(typed_level2_text, True, TEXT_COLOR)
        level2_display_text_rect = level2_display_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(level2_display_text, level2_display_text_rect)
        
        if typing_index_level2 >= 558:
            # Draw "Option 1" button
            pygame.draw.rect(screen, BUTTON_BORDER_COLOR, option1_button_rect)
            pygame.draw.rect(screen, BUTTON_COLOR, option1_button_rect, border_radius=BUTTON_RADIUS)

            option1_button_text = font_small_button.render("devongames", True, BUTTON_TEXT_COLOR)
            option1_button_text_rect = option1_button_text.get_rect(center=option1_button_rect.center)
            screen.blit(option1_button_text, option1_button_text_rect)

            # Draw "Option 2" button
            pygame.draw.rect(screen, BUTTON_BORDER_COLOR, option2_button_rect)
            pygame.draw.rect(screen, BUTTON_COLOR, option2_button_rect, border_radius=BUTTON_RADIUS)

            option2_button_text = font_small_button.render("vU2!dm@Kf&95#", True, BUTTON_TEXT_COLOR)
            option2_button_text_rect = option2_button_text.get_rect(center=option2_button_rect.center)
            screen.blit(option2_button_text, option2_button_text_rect)
            
    elif game_state == "level2_1":
        # Clear the screen
        screen.fill(BG_COLOR)

        # Display Level 3 text
        level2_1_text = '''Devon has been playing the game for a couple of weeks now, and he even participates in online tournaments against other players.'''
        level2_1_display_text = font_small_button.render(level2_1_text, True, TEXT_COLOR)
        level2_1_display_text_rect = level2_1_display_text.get_rect(center=(WIDTH // 2, 300))
        screen.blit(level2_1_display_text, level2_1_display_text_rect)

    elif game_state == "level2_2":
        # Clear the screen
        screen.fill(BG_COLOR)

        # Display Level 4 text
        level2_2_text = '''Devon has been playing the game for a couple of weeks now, and he’s on a 30-day streak of completing his daily challenges in the app.
        There was a power outage in his neighborhood and he’s worried that he’ll lose his streak if he does not complete his challenge.
        So he messages his best friend, Michael, and asks him to log into his account and complete his challenge for him. Michael says that he’ll do it and asks Devon
        to send the password to his account. What should Devon do?'''
        # Wrap the text
        wrapped_text: list = []
        for line in level2_2_text.splitlines():
            wrapped_text.extend(textwrap.wrap(line, width=MAX_LINE_WIDTH))

        '''level4_display_text = font_small_button.render(level4_text, True, TEXT_COLOR)
        level4_display_text_rect = level4_display_text.get_rect(center=(WIDTH // 2, 300))
        screen.blit(level4_display_text, level4_display_text_rect)'''
        y_position = 50  # Adjust the vertical position
        for line in wrapped_text:
            line_surface = font_text.render(line, True, TEXT_COLOR)
            text_width, text_height = line_surface.get_size()
            screen.blit(line_surface, ((WIDTH - text_width) // 2, y_position))
            y_position += text_height + 5  # Adjust the vertical spacing

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()