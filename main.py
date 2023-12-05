import os
import random
import pygame
from pygame.locals import *

# Set the path to your image folder
image_folder = "./questions/"
answer_folder = "./answers/"

# Get a list of all image files in the folder
image_files = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Random Image Viewer")

# Set the background color to white
background_color = (255, 255, 255)

# Function to load and display a scaled image
def display_image(image_path):
    screen.fill(background_color)  # Fill the screen with the background color

    original_image = pygame.image.load(image_path)
    original_width, original_height = original_image.get_size()

    # Calculate the scaling factor to fit the image on the screen
    scale_factor = min(screen_width / original_width, screen_height / original_height)
    
    # Scale the image
    scaled_width = int(original_width * scale_factor)
    scaled_height = int(original_height * scale_factor)
    scaled_image = pygame.transform.scale(original_image, (scaled_width, scaled_height))

    # Center the scaled image on the screen
    x = (screen_width - scaled_width) // 2
    y = (screen_height - scaled_height) // 2

    screen.blit(scaled_image, (x, y))
    pygame.display.flip()

# Display the first random image
current_image = random.choice(image_files)
image_path = os.path.join(image_folder, current_image)
display_image(image_path)

running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                # Display another random image
                current_image = random.choice(image_files)
                image_path = os.path.join(image_folder, current_image)
                display_image(image_path)
            elif event.key == K_RETURN:
                # Go to the answers folder and display the corresponding image
                answer_path = os.path.join(answer_folder, current_image)
                if os.path.isfile(answer_path):
                    display_image(answer_path)
                else:
                    print(f"No answer found for {current_image}")
        elif event.type == QUIT:
            running = False

pygame.quit()
