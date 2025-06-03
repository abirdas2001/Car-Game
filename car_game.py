import pygame
import sys
import random

pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Game")

# Load images
road_img = pygame.image.load('road.png')
car_img = pygame.image.load('player_car.png')
obstacle_img = pygame.image.load('obstacle_car.png')

# Scale images if needed
road_img = pygame.transform.scale(road_img, (WIDTH, HEIGHT))
car_img = pygame.transform.scale(car_img, (120,120))
obstacle_img = pygame.transform.scale(obstacle_img, (120,120))

# Initial positions
car_x, car_y = WIDTH // 2 - 30, HEIGHT - 150
obstacle_x, obstacle_y = WIDTH // 2 - 30, 0

clock = pygame.time.Clock()
speed = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= speed
    if keys[pygame.K_RIGHT] and car_x < WIDTH - 60:
        car_x += speed
    if keys[pygame.K_UP] and car_y > 0:
        car_y -= speed
    if keys[pygame.K_DOWN] and car_y < HEIGHT - 120:
        car_y += speed

    # Move obstacle randomly down the screen
    obstacle_y += speed  # Move obstacle down

    # If obstacle goes off the screen, reset to top at a random x position
    if obstacle_y > HEIGHT:
        obstacle_y = -120  # Start just above the screen
        obstacle_x = random.randint(0, WIDTH - 120)  # Random horizontal position


    # Collision Detection
    if (car_x < obstacle_x + 60 and car_x + 60 > obstacle_x) and (car_y < obstacle_y + 120 and car_y + 120 > obstacle_y):
        print("Collision Detected! Game Over.")
        pygame.quit()
        sys.exit()

    # Draw everything
    screen.blit(road_img, (0, 0))
    screen.blit(car_img, (car_x, car_y))
    screen.blit(obstacle_img, (obstacle_x, obstacle_y))

    pygame.display.flip()
    clock.tick(60)