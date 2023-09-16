import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
FONT = pygame.font.Font(None, 36)

# Colors
WHITE = (255, 255, 255)
BUTTON_COLOR = (0, 128, 255)
BUTTON_TEXT_COLOR = (255, 255, 255)

# Define pages and decisions
pages = {
    1: {"text": "You find a fork in the road. Which path do you choose?", "options": ["Left", "Right"], "goto": [2, 3]},
    2: {"text": "You encounter a friendly troll. What do you do?", "options": ["Talk to the troll", "Ignore the troll"], "goto": [4, 5]},
    3: {"text": "You come across a deep river. How do you cross it?", "options": ["Swim", "Build a raft"], "goto": [6, 7]},
    4: {"text": "The troll gives you a magical key. You continue on your journey.", "options": ["yes","no"], "goto": [1,6]},
    5: {"text": "You decide to ignore the troll and move forward.", "options": ["ye2s","nso"], "goto": [5,4]},
    6: {"text": "You swim across the river but are exhausted. You continue on your journey.", "options": ["yegs","n2o"], "goto": [7,2]},
    7: {"text": "You build a raft and safely cross the river. You continue on your journey.", "options": ["ybes","n1o"], "goto": [1,6]},
}

# Class for creating buttons
class Button:
    def __init__(self, text, x, y, width, height, callback):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.callback = callback
        self.clicked = False
    
    def draw(self):
        pygame.draw.rect(SCREEN, BUTTON_COLOR, self.rect)
        text_surface = FONT.render(self.text, True, BUTTON_TEXT_COLOR)
        text_rect = text_surface.get_rect(center=self.rect.center)
        SCREEN.blit(text_surface, text_rect)
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.clicked = True
                if self.callback:
                    self.callback()

# Function to create buttons for options
def create_option_buttons(options, screen_height):
    button_width, button_height = 200, 50
    button_spacing = 20
    total_height = (button_height + button_spacing) * len(options)
    y_start = (screen_height - total_height) // 2
    buttons = []
    
    for option in options:
        button = Button(option, (SCREEN.get_width() - button_width) // 2, y_start, button_width, button_height, None)
        buttons.append(button)
        y_start += button_height + button_spacing
    
    return buttons

# Create the screen
current_page = 1
running = True
buttons = []

def on_option_selected(option_index):
    global current_page
    page_info = pages[current_page]
    current_page = page_info["goto"][option_index]

# Dynamically set screen size based on content
max_text_width = max(FONT.size(page_info["text"])[0] for page_info in pages.values())
max_button_width = max(FONT.size(option)[0] for page_info in pages.values() if "options" in page_info for option in page_info["options"])
screen_width = max(max_text_width, max_button_width) + 40
screen_height = pygame.display.Info().current_h  # Use the current screen height

SCREEN = pygame.display.set_mode((screen_width, screen_height))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        for button in buttons:
            button.handle_event(event)
    
    SCREEN.fill(WHITE)
    
    page_info = pages[current_page]
    text_surface = FONT.render(page_info["text"], True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(SCREEN.get_width() // 2, SCREEN.get_height() * 0.3))
    SCREEN.blit(text_surface, text_rect)
    
    if current_page in pages and "options" in pages[current_page]:
        buttons = create_option_buttons(page_info["options"], screen_height)
        for i, button in enumerate(buttons):
            button.callback = lambda option_index=i: on_option_selected(option_index)
    
    for button in buttons:
        button.draw()
    
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
