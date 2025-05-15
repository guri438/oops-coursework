import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Dodger Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Player properties
player_size = 50
player_y = screen_height - player_size - 20
player_speed = 5

# Obstacle properties
obstacle_size = 30
obstacle_speed = 3
obstacles = []  # List to store obstacle rectangles
obstacle_spawn_rate = 60  # Spawn a new obstacle every this many frames
obstacle_spawn_counter = 0

# Score
score = 0
font = pygame.font.Font(None, 36)

def draw_player(x, y):
    pygame.draw.rect(screen, black, (x, y, player_size, player_size))

def draw_obstacle(obstacle):
    pygame.draw.rect(screen, red, obstacle)

def display_score():
    score_text = font.render(f"Score: {score}", True, black)
    screen.blit(score_text, (10, 10))

def game_over_screen():
    game_over_text = font.render("Game Over", True, red)
    score_text = font.render(f"Final Score: {score}", True, black)
    restart_text = font.render("Press SPACE to restart", True, black)

    game_over_rect = game_over_text.get_rect(center=(screen_width // 2, screen_height // 3))
    score_rect = score_text.get_rect(center=(screen_width // 2, screen_height // 2))
    restart_rect = restart_text.get_rect(center=(screen_width // 2, screen_height * 2 // 3))

    screen.blit(game_over_text, game_over_rect)
    screen.blit(score_text, score_rect)
    screen.blit(restart_text, restart_rect)
    pygame.display.flip()

    waiting_for_restart = True
    while waiting_for_restart:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting_for_restart = False
                    return True  # Signal to restart
    return False

def game():
    global obstacles, score, obstacle_spawn_counter

    running = True
    game_over = False
    player_x = screen_width // 2 - player_size // 2
    obstacles = []
    score = 0
    obstacle_spawn_counter = 0

    clock = pygame.time.Clock()

    while running:
        screen.fill(white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed

        # Keep player within screen bounds
        if player_x < 0:
            player_x = 0
        elif player_x > screen_width - player_size:
            player_x = screen_width - player_size

        # Spawn new obstacles
        obstacle_spawn_counter += 1
        if obstacle_spawn_counter >= obstacle_spawn_rate:
            obstacle_spawn_counter = 0
            obstacle_x = random.randint(0, screen_width - obstacle_size)
            obstacle_y = -obstacle_size
            obstacles.append(pygame.Rect(obstacle_x, obstacle_y, obstacle_size, obstacle_size))

        # Move obstacles
        for obstacle in obstacles[:]:
            obstacle.y += obstacle_speed
            if obstacle.bottom > screen_height:
                obstacles.remove(obstacle)
                score += 1

        # Collision detection
        player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
        for obstacle in obstacles:
            if player_rect.colliderect(obstacle):
                game_over = True
                break

        draw_player(player_x, player_y)
        for obstacle in obstacles:
            draw_obstacle(obstacle)
        display_score()

        pygame.display.flip()

        if game_over:
            if game_over_screen():
                game()
            else:
                running = False

        clock.tick(60)

    pygame.quit()

# Corrected entry point
if __name__ == "__main__":
    game()
