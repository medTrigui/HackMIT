import pygame
import sys
import textwrap

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1366, 766
BG_COLOR = (0, 0, 0)        # Black
TEXT_COLOR = (255, 255, 255)   # White
BUTTON_COLOR = (255, 0, 0)  # Red
BUTTON_TEXT_COLOR = (255, 255, 255)  # White
BUTTON_BORDER_COLOR = (0, 0, 0)  # Dark Blue
BUTTON_HOVER_COLOR = (255, 255, 255)  # Light Blue
BUTTON_HOVER_TEXT_COLOR = (255, 255, 255)  # White
BUTTON_WIDTH, BUTTON_HEIGHT = 200, 50
BUTTON_RADIUS = 10
SMALL_BUTTON_WIDTH, SMALL_BUTTON_HEIGHT = 50, 30
MAX_LINE_WIDTH = 400

# Create the Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cyber Awareness Game")

# Load fonts
font_title = pygame.font.Font(None, 56)  # Use the default font ("Courier")
font_button = pygame.font.Font(None, 36)
font_text = pygame.font.Font(None, 24)
font_small_button = pygame.font.Font(None, 18)


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


# Game state
game_state = "menu"  # Initial state is the menu


# Text typing effect
#typing_effect_text = '''Introduction: In an era of constantly evolving cybersecurity threats, the digital landscape presents ever-increasing challenges. Every year, new and more sophisticated forms of malware emerge, putting individuals' personal information and digital security at risk. Whether it's safeguarding your passwords, staying vigilant against phishing attempts, protecting your data, or navigating the internet securely. The choices you make in your daily online life can have significant consequences. In this series, we embark on a journey to impart essential knowledge about password security, phishing awareness, data protection, and safe internet usage. Our aim is to engage and educate you in a fun and interactive manner, empowering you to navigate the digital realm with confidence. By arming yourself with these skills, you can effectively thwart cybercriminals' traps and safeguard your personal information in today's ever-evolving digital world.'''
'''typed_text = ""
text_speed = 35  # Adjust the speed by changing the delay (lower value for faster typing)
typing_index = 0
typing_timer = pygame.time.get_ticks()

# Create a list of lines by splitting the text at the line breaks
typed_lines = textwrap.w
rap(typing_effect_text, width=60)'''


# Level 2 text
#level2_text = '''Devon has been counting down to the release of the new CyberRunner video game, an immersive experience where the player gets to simulate being an ethical hacker. He stays up all night thinking of what his username is going to be. After hours of thinking, he finally comes up with a username and goes to bed. When he wakes up, he excitedly turns on his console, but when prompted with creating an account, he realizes that although he thought thoroughly about the username, he forgot an important piece of information - the password. What password should he use?'''
'''typed_level2_text = ""
text_speed_level2 = 35  # Adjust the speed by changing the delay (lower value for faster typing)
typing_index_level2 = 0
typing_timer_level2 = pygame.time.get_ticks()'''

# Main loop
running = True
line_index = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if start_button_rect.collidepoint(event.pos):
                if game_state == "menu":
                    game_state = "level1"
                elif game_state == "level1":
                    '''
                    # Display the sentences with word wrapping
                    current_time = pygame.time.get_ticks()
                    if current_time - typing_timer > text_speed and typing_index < len(typing_effect_text):
                        typed_text += typing_effect_text[typing_index]
                        typing_index += 1
                        typing_timer = current_time

                        # Check if the typed text exceeds the screen width
                        if font_button.size(typed_text)[0] > WIDTH - 40:  # Adjust the padding as needed
                        # Move to the next line
                            typed_text += "\n"'''
                    level1_text = font_button.render(typed_text, True, TEXT_COLOR)
                    level1_text_rect = level1_text.get_rect(topleft=(20, 20))  # Adjust the position as needed
                    screen.blit(level1_text, level1_text_rect)

        
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
        
        elif game_state == "level2_1" and continue_button_rect.collidepoint(event.pos):
            game_state = "level3"
        
        elif game_state == "level2_2" and continue_button_rect.collidepoint(event.pos):
            game_state = "level3"
        
        elif game_state == "level3":
            if option1_button_rect.collidepoint(event.pos):
                # Handle clicking "Option 1" to transition to Level 3_1
                game_state = "level3_1"
            elif option2_button_rect.collidepoint(event.pos):
                # Handle clicking "Option 2" to transition to Level 3_2
                game_state = "level3_2"

        elif game_state == "level3_1" and continue_button_rect.collidepoint(event.pos):
            game_state = "level4"

        elif game_state == "level3_2" and continue_button_rect.collidepoint(event.pos):
            game_state = "level4"
        
        elif game_state == "level4":
            if option1_button_rect.collidepoint(event.pos):
                # Handle clicking "Option 1" to transition to Level 3_1
                game_state = "level4_1"
            elif option2_button_rect.collidepoint(event.pos):
                # Handle clicking "Option 2" to transition to Level 3_2
                game_state = "level4_2"

        
        

    # Clear the screen
    screen.fill(BG_COLOR)

    if game_state == "menu":
        # Display the welcome message
        welcome_text = font_title.render("SecurEscape: The Cyber Chronicles", True, TEXT_COLOR)
        welcome_text_rect = welcome_text.get_rect(center=(WIDTH // 2, 150))
        screen.blit(welcome_text, welcome_text_rect)


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


    elif game_state == "level1":
        
        # Display the level 1 message with a typing effect
        '''current_time = pygame.time.get_ticks()
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
            typing_index = 0'''
        # Clear the screen
        screen.fill(BG_COLOR)

        lev1_text = '''Introduction: In an era of constantly evolving cybersecurity threats, the digital landscape presents ever-increasing challenges. 
        Every year, new and more sophisticated forms of malware emerge, putting individuals' personal information and digital security at risk. 
        Whether it's safeguarding your passwords, staying vigilant against phishing attempts, protecting your data, or navigating the internet securely. 
        The choices you make in your daily online life can have significant consequences. 
        In this series, we embark on a journey to impart essential knowledge about password security, phishing awareness, data protection, and safe internet usage. 
        Our aim is to engage and educate you in a fun and interactive manner, empowering you to navigate the digital realm with confidence. 
        By arming yourself with these skills, you can effectively thwart cybercriminals' traps and safeguard your personal information in today's ever-evolving digital world.'''
        
        # Wrap the text
        wrapped_text: list = []
        for line in lev1_text.splitlines():
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
        level2_text = '''Devon has been counting down to the release of the new CyberRunner video game, an immersive experience where the player gets 
        to simulate being an ethical hacker. He stays up all night thinking of what his username is going to be. After hours of thinking, he finally comes up 
        with a username and goes to bed. When he wakes up, he excitedly turns on his console, but when prompted with creating an account. 
        He realizes that although he thought thoroughly about the username, he forgot an important piece of information - the password. What password should he use?'''
        '''current_time_level2 = pygame.time.get_ticks()
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
            screen.blit(option1_button_text, option1_button_text_rect)'''
        # Wrap the text
        wrapped_text: list = []
        for line in level2_text.splitlines():
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

        # Display Level2_1 text
        level2_1_text = '''Devon has been playing the game for a couple of weeks now, and he even participates in online tournaments against other players. 
        However, he came across a player who just couldn’t handle defeat. The player was quite tech-savvy, and ended up hacking Devon’s account. 
        
        This cautionary tale underscores the importance of choosing a robust and secure password, as Devon's lackluster choice left his account vulnerable to compromise.'''
        
        
        # Wrap the text
        wrapped_text: list = []
        for line in level2_1_text.splitlines():
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

        # Draw the "Continue" button in Level 2_1
        pygame.draw.rect(screen, BUTTON_BORDER_COLOR, continue_button_rect)
        pygame.draw.rect(screen, BUTTON_COLOR, continue_button_rect, border_radius=BUTTON_RADIUS)

        if continue_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, BUTTON_HOVER_COLOR, continue_button_rect, border_radius=BUTTON_RADIUS)
            continue_button_text = font_small_button.render("Continue", True, BUTTON_HOVER_TEXT_COLOR)
        else:
            continue_button_text = font_small_button.render("Continue", True, BUTTON_TEXT_COLOR)

        continue_button_text_rect = continue_button_text.get_rect(center=continue_button_rect.center)
        screen.blit(continue_button_text, continue_button_text_rect)

    elif game_state == "level2_2":
        # Clear the screen
        screen.fill(BG_COLOR)

        # Display Level2_2 text
        level2_2_text = '''Devon has been gaming for a couple of weeks now, even diving into online tournaments with other players. 
        However, he encountered a player who couldn't handle defeat. This tech-savvy opponent attempted to hack Devon's account for revenge. 
        Fortunately, Devon's choice of a strong password thwarted the hacker's mission, allowing him to keep his account secure.
        Moral: Choosing a robust password reduces the risk of hacking and safeguards your account."'''
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

        # Draw the "Continue" button in Level 2_2
        pygame.draw.rect(screen, BUTTON_BORDER_COLOR, continue_button_rect)
        pygame.draw.rect(screen, BUTTON_COLOR, continue_button_rect, border_radius=BUTTON_RADIUS)

        if continue_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, BUTTON_HOVER_COLOR, continue_button_rect, border_radius=BUTTON_RADIUS)
            continue_button_text = font_small_button.render("Continue", True, BUTTON_HOVER_TEXT_COLOR)
        else:
            continue_button_text = font_small_button.render("Continue", True, BUTTON_TEXT_COLOR)

        continue_button_text_rect = continue_button_text.get_rect(center=continue_button_rect.center)
        screen.blit(continue_button_text, continue_button_text_rect)

    elif game_state == "level3":
        # Clear the screen
        screen.fill(BG_COLOR)

        # Display Level3 text
        level3_text = '''In the vibrant tapestry of digital friendships, the story of Devon and Michael unfolds with a unique twist. 
        Devon had been on an impressive 30-day streak of successfully completing his daily challenges in a popular gaming app. 
        This streak had become a source of pride and accomplishment for him, a testament to his dedication and skill in the virtual realm.
        However, fate threw a curveball at Devon when a power outage struck his neighborhood, plunging his world into darkness. 
        Panic set in as he realized that his unblemished streak was now at risk of breaking if he couldn't complete his challenge for the day. 
        Desperate to maintain his hard-earned record, Devon found himself at a crossroads.
        In this moment of vulnerability and uncertainty, his friend Michael extended a helping hand, albeit one that carried a dilemma. 
        Michael, knowing the importance of Devon's streak, made an audacious request – he asked Devon to share his password so that he could 
        log into Devon's account and complete the challenge on his behalf.
        Devon, faced with an online gaming dilemma, made the decision to confide in his friend Michael by sharing his precious account password. '''

        # Wrap the text
        wrapped_text: list = []
        for line in level3_text.splitlines():
            wrapped_text.extend(textwrap.wrap(line, width=MAX_LINE_WIDTH))

        y_position = 50  # Adjust the vertical position
        for line in wrapped_text:
            line_surface = font_text.render(line, True, TEXT_COLOR)
            text_width, text_height = line_surface.get_size()
            screen.blit(line_surface, ((WIDTH - text_width) // 2, y_position))
            y_position += text_height + 5  # Adjust the vertical spacing

        # Draw "Option 1" button
        pygame.draw.rect(screen, BUTTON_BORDER_COLOR, option1_button_rect)
        pygame.draw.rect(screen, BUTTON_COLOR, option1_button_rect, border_radius=BUTTON_RADIUS)

        option1_button_text = font_small_button.render("Send pwd", True, BUTTON_TEXT_COLOR)
        option1_button_text_rect = option1_button_text.get_rect(center=option1_button_rect.center)
        screen.blit(option1_button_text, option1_button_text_rect)

        # Draw "Option 2" button
        pygame.draw.rect(screen, BUTTON_BORDER_COLOR, option2_button_rect)
        pygame.draw.rect(screen, BUTTON_COLOR, option2_button_rect, border_radius=BUTTON_RADIUS)

        option2_button_text = font_small_button.render("Do not send", True, BUTTON_TEXT_COLOR)
        option2_button_text_rect = option2_button_text.get_rect(center=option2_button_rect.center)
        screen.blit(option2_button_text, option2_button_text_rect)

    elif game_state == "level3_1":
        lev3_1_text = '''Devon made the decision to confide in his friend Michael by sharing his precious account password. 
        His trust in Michael was unwavering, believing that their bond transcended the virtual world.
        As Michael accessed Devon's account, his intentions were nothing but pure – to lend a hand to his friend in need. 
        Little did they know, their actions would set off a chain of events that would impart a profound lesson.

        Within the gaming universe, a vigilant anti-cheat system stood watchful. It detected Michael's login on a separate device, 
        a seemingly innocuous act in their eyes. However, the anti-cheat system had a higher purpose: to ensure the integrity of the
        game and the fairness of its challenges. It swiftly administered a ban to Devon's account, citing a violation of its strict 
        policy against account sharing. The message was clear – in this gaming world, another player couldn't complete your challenges for you.

        This story underscores a crucial moral lesson: trust, though invaluable, must always be balanced with responsibility. 
        It serves as a stark reminder that our actions, even with the purest of intentions, can lead to unintended consequences. 
        It teaches us that trust should be grounded not just in faith in others but also in an understanding of the rules and systems that govern the spaces we interact in.
        
        The moral of the story emphasizes the importance of respecting the rules and guidelines of any community or platform we engage with, 
        whether it be in the digital realm or the physical world. It underscores the notion that trust, while a powerful bond, should always 
        be coupled with a keen awareness of the potential consequences of our actions. In a world that is increasingly interconnected, we must 
        navigate the delicate balance between trust and responsibility, ensuring that our actions do not inadvertently lead to the downfall of those we care about.'''
        # Wrap the text
        wrapped_text: list = []
        for line in lev3_1_text.splitlines():
            wrapped_text.extend(textwrap.wrap(line, width=MAX_LINE_WIDTH))

        y_position = 50  # Adjust the vertical position
        for line in wrapped_text:
            line_surface = font_text.render(line, True, TEXT_COLOR)
            text_width, text_height = line_surface.get_size()
            screen.blit(line_surface, ((WIDTH - text_width) // 2, y_position))
            y_position += text_height + 5  # Adjust the vertical spacing

        # Draw the "Continue" button in Level 3_1
        pygame.draw.rect(screen, BUTTON_BORDER_COLOR, continue_button_rect)
        pygame.draw.rect(screen, BUTTON_COLOR, continue_button_rect, border_radius=BUTTON_RADIUS)

        if continue_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, BUTTON_HOVER_COLOR, continue_button_rect, border_radius=BUTTON_RADIUS)
            continue_button_text = font_small_button.render("Continue", True, BUTTON_HOVER_TEXT_COLOR)
        else:
            continue_button_text = font_small_button.render("Continue", True, BUTTON_TEXT_COLOR)

        continue_button_text_rect = continue_button_text.get_rect(center=continue_button_rect.center)
        screen.blit(continue_button_text, continue_button_text_rect)

    elif game_state == "level3_2":
        lev3_2_text = '''As the story unfolds, we witness a pivotal moment. Devon, with a wise and cautious demeanor, makes the conscious 
        decision not to share his password. He recognizes the importance of safeguarding his personal information and secures his account.

        This story serves as a powerful reminder of the significance of online security and the value of trust in our digital interactions. 
        The moral of the story teaches us that even with the best intentions, it is crucial to prioritize the protection of our online identities. 
        Trust should always be accompanied by responsible practices, and securing our accounts is a responsibility we all share. 
        In this era of interconnectedness, the lesson is clear: Guard your online presence like a treasure, and let trust be built on a foundation of caution and cybersecurity.'''
        # Wrap the text
        wrapped_text: list = []
        for line in lev3_2_text.splitlines():
            wrapped_text.extend(textwrap.wrap(line, width=MAX_LINE_WIDTH))

        y_position = 50  # Adjust the vertical position
        for line in wrapped_text:
            line_surface = font_text.render(line, True, TEXT_COLOR)
            text_width, text_height = line_surface.get_size()
            screen.blit(line_surface, ((WIDTH - text_width) // 2, y_position))
            y_position += text_height + 5  # Adjust the vertical spacing
        # Draw the "Continue" button in Level 3_2
        pygame.draw.rect(screen, BUTTON_BORDER_COLOR, continue_button_rect)
        pygame.draw.rect(screen, BUTTON_COLOR, continue_button_rect, border_radius=BUTTON_RADIUS)

        if continue_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, BUTTON_HOVER_COLOR, continue_button_rect, border_radius=BUTTON_RADIUS)
            continue_button_text = font_small_button.render("Continue", True, BUTTON_HOVER_TEXT_COLOR)
        else:
            continue_button_text = font_small_button.render("Continue", True, BUTTON_TEXT_COLOR)

        continue_button_text_rect = continue_button_text.get_rect(center=continue_button_rect.center)
        screen.blit(continue_button_text, continue_button_text_rect)

    elif game_state == "level4":
        lev4_text = '''In the digital landscape of Devon's online life, an in-game notification appeared on his screen, gently suggesting 
                       that he update his password. It had been 90 days since he first created his gaming account, and the system, ever watchful
                       for his security, recommended a change. However, Devon hesitated, for he had been using this same password for all his 
                       accounts - from social media platforms to multiple email accounts - for the past three years. It had become his digital companion, 
                       and he believed he could never forget it. '''
        # Wrap the text
        wrapped_text: list = []
        for line in lev4_text.splitlines():
            wrapped_text.extend(textwrap.wrap(line, width=MAX_LINE_WIDTH))

        y_position = 50  # Adjust the vertical position
        for line in wrapped_text:
            line_surface = font_text.render(line, True, TEXT_COLOR)
            text_width, text_height = line_surface.get_size()
            screen.blit(line_surface, ((WIDTH - text_width) // 2, y_position))
            y_position += text_height + 5  # Adjust the vertical spacing
        # Draw "Option 1" button
        pygame.draw.rect(screen, BUTTON_BORDER_COLOR, option1_button_rect)
        pygame.draw.rect(screen, BUTTON_COLOR, option1_button_rect, border_radius=BUTTON_RADIUS)

        option1_button_text = font_small_button.render("Ignore notification", True, BUTTON_TEXT_COLOR)
        option1_button_text_rect = option1_button_text.get_rect(center=option1_button_rect.center)
        screen.blit(option1_button_text, option1_button_text_rect)

        # Draw "Option 2" button
        pygame.draw.rect(screen, BUTTON_BORDER_COLOR, option2_button_rect)
        pygame.draw.rect(screen, BUTTON_COLOR, option2_button_rect, border_radius=BUTTON_RADIUS)

        option2_button_text = font_small_button.render("Update password", True, BUTTON_TEXT_COLOR)
        option2_button_text_rect = option2_button_text.get_rect(center=option2_button_rect.center)
        screen.blit(option2_button_text, option2_button_text_rect)
    
    elif game_state == "level4_1":
        lev4_1_text = '''Amidst the ordinary ebb and flow of life, a sudden jolt of shock and dismay seized Devon's senses. 
                        On a seemingly uneventful day, he stumbled upon a chilling discovery: his beloved Instagram account 
                        had fallen victim to a malicious hacker. But what sent shivers down his spine was the dreadful realization 
                        that this cyber infiltrator had managed to breach not just one, but all of his online accounts - a domino 
                        effect unleashed by the use of a uniform password. This unexpected turn of events thrust Devon into a harrowing 
                        dilemma, one that carried profound lessons:

                        Moral of the Story:
                        Devon's ordeal underscores a critical lesson for the digital age - the perils of complacency and the importance 
                        of safeguarding one's digital identity. His unwavering trust in a single, easily remembered password had unwittingly
                        opened the door to a cascade of security breaches.
                        The story serves as a stark reminder that in a world where technology is an integral part of our lives, maintaining good 
                        password hygiene and adopting robust cybersecurity practices is paramount. The convenience of a familiar password should 
                        never overshadow the necessity of diversifying and regularly updating them.
                        Devon's experience teaches us that the repercussions of lax cybersecurity can extend far beyond a single account. 
                        It illuminates the truth that the keys to our digital lives, once compromised, can unlock a treasure trove of sensitive 
                        information and wreak havoc on our online existence. Ultimately, the moral here is crystal clear: Take proactive steps 
                        to protect your digital presence, for in the world of the internet, a strong defense is the guardian of your virtual realm.'''
        # Wrap the text
        wrapped_text: list = []
        for line in lev4_1_text.splitlines():
            wrapped_text.extend(textwrap.wrap(line, width=MAX_LINE_WIDTH))

        y_position = 50  # Adjust the vertical position
        for line in wrapped_text:
            line_surface = font_text.render(line, True, TEXT_COLOR)
            text_width, text_height = line_surface.get_size()
            screen.blit(line_surface, ((WIDTH - text_width) // 2, y_position))
            y_position += text_height + 5  # Adjust the vertical spacing

    elif game_state == "level4_2":
        lev4_2_text = '''Congratulations! You've successfully safeguarded your digital realm through the diligent practice of effective password 
        protection techniques. In a world where the boundaries between our physical and digital lives blur, the significance of securing our 
        online identities cannot be overstated. Your commitment to cybersecurity best practices has paid off handsomely, and it's a testament 
        to your wisdom in navigating the ever-evolving landscape of the internet.
        By regularly updating and diversifying your passwords, you've erected a formidable barrier against potential intruders. Your willingness 
        to embrace the complexities of unique, hard-to-crack passwords has proven instrumental in fending off cyber threats.
        But your achievement extends beyond passwords alone. Your vigilance in recognizing the importance of two-factor authentication, 
        utilizing trusted password managers, and staying informed about the latest cybersecurity trends has fortified your digital fortress.

        In essence, your dedication to good password protection techniques is a shining example of how individual responsibility and proactive 
        measures can triumph over the lurking shadows of cyberattacks. It demonstrates that, in the digital age, knowledge, and vigilance are the
        cornerstones of a secure online existence. As you continue to navigate the vast digital seas, remember that your commitment 
        to cybersecurity serves not only as a shield for your online presence but also as an inspiration to others in the ongoing battle to 
        safeguard our interconnected world.'''
        # Wrap the text
        wrapped_text: list = []
        for line in lev4_2_text.splitlines():
            wrapped_text.extend(textwrap.wrap(line, width=MAX_LINE_WIDTH))

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