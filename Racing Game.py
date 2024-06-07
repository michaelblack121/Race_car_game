import pygame
import random
# hello!

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("A CRAZY RACING EXPERIENCE")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
GRAY = (169, 169, 169)
DARK_GRAY = (105, 105, 105)
ORANGE = (255, 165, 0)
PINK = (255, 0, 255)
GRASS = (245, 245, 245)
DARK_GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)

# Car settings
car_width, car_height = 60, 120
car_speed = 5

# Enemy settings
enemy_width, enemy_height = 60, 120
enemy_speed = 5

# Font settings
font = pygame.font.Font(None, 74)
button_font = pygame.font.Font(None, 50)

# Winning score
WINNING_SCORE = 100

# Function to draw the player's car
def draw_car(x, y):
    # Main body
    pygame.draw.rect(screen, ORANGE, [x, y, car_width, car_height])

    # Roof
    roof_width = car_width * 0.8
    roof_height = car_height * 0.5
    roof_x = x + (car_width - roof_width) / 2
    roof_y = y + (car_height - roof_height) / 2
    pygame.draw.rect(screen, PURPLE, [roof_x, roof_y, roof_width, roof_height])

    # Wheels
    wheel_width = 10
    wheel_height = 20
    # Front left wheel
    pygame.draw.rect(screen, GRAY, [x - wheel_width, y + 10, wheel_width, wheel_height])
    # Front right wheel
    pygame.draw.rect(screen, GRAY, [x + car_width, y + 10, wheel_width, wheel_height])
    # Rear left wheel
    pygame.draw.rect(screen, GRAY, [x - wheel_width, y + car_height - 30, wheel_width, wheel_height])
    # Rear right wheel
    pygame.draw.rect(screen, GRAY, [x + car_width, y + car_height - 30, wheel_width, wheel_height])

# Function to draw the enemy car
def draw_enemy(x, y):
    # Main body
    pygame.draw.rect(screen, BLUE, [x, y, enemy_width, enemy_height])

    # Roof
    roof_width = enemy_width * 0.8
    roof_height = enemy_height * 0.5
    roof_x = x + (enemy_width - roof_width) / 2
    roof_y = y + (enemy_height - roof_height) / 2
    pygame.draw.rect(screen, YELLOW, [roof_x, roof_y, roof_width, roof_height])

    # Wheels
    wheel_width = 10
    wheel_height = 20
    # Front left wheel
    pygame.draw.rect(screen, GRAY, [x - wheel_width, y + 10, wheel_width, wheel_height])
    # Front right wheel
    pygame.draw.rect(screen, GRAY, [x + enemy_width, y + 10, wheel_width, wheel_height])
    # Rear left wheel
    pygame.draw.rect(screen, GRAY, [x - wheel_width, y + enemy_height - 30, wheel_width, wheel_height])
    # Rear right wheel
    pygame.draw.rect(screen, GRAY, [x + enemy_width, y + enemy_height - 30, wheel_width, wheel_height])

# Function to draw the button
def draw_button(text, x, y, width, height, inactive_color, active_color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(screen, active_color, [x, y, width, height])
        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(screen, inactive_color, [x, y, width, height])

    text_surf = button_font.render(text, True, BLACK)
    text_rect = text_surf.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surf, text_rect)

# Main menu loop with animation
def main_menu():
    menu = True
    title_y = HEIGHT // 3
    direction = 1

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(GRASS)
        title = font.render("A CRAZY RACING EXPERIENCE", True, BLACK)
        title_rect = title.get_rect(center=(WIDTH // 2, title_y))
        screen.blit(title, title_rect)

        draw_button("Start Game", WIDTH // 2 - 100, HEIGHT // 2, 200, 50, GREEN, DARK_GRAY, game_loop)

        pygame.display.update()

        # Animate the title
        title_y += direction
        if title_y <= HEIGHT // 3 - 10 or title_y >= HEIGHT // 3 + 10:
            direction *= -1

# Game over screen
def game_over():
    over = True
    while over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(GRAY)
        game_over_text = font.render("Game Over", True, BLACK)
        game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 3))
        screen.blit(game_over_text, game_over_rect)

        draw_button("Restart Game", WIDTH // 2 - 100, HEIGHT // 2, 200, 50, GREEN, DARK_GRAY, game_loop)
        draw_button("Main Menu", WIDTH // 2 - 100, HEIGHT // 2 + 70, 200, 50, GREEN, DARK_GRAY, main_menu)

        pygame.display.update()

# You win screen
def you_win():
    win = True
    while win:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(GRAY)
        you_win_text = font.render("You Win!", True, BLACK)
        you_win_rect = you_win_text.get_rect(center=(WIDTH // 2, HEIGHT // 3))
        screen.blit(you_win_text, you_win_rect)

        draw_button("Restart Game", WIDTH // 2 - 100, HEIGHT // 2, 200, 50, GREEN, DARK_GRAY, game_loop)
        draw_button("Main Menu", WIDTH // 2 - 100, HEIGHT // 2 + 70, 200, 50, GREEN, DARK_GRAY, main_menu)

        pygame.display.update()

# Main game loop
def game_loop():
    x = WIDTH * 0.45
    y = HEIGHT * 0.8
    x_change = 0

    enemy_start_x = random.randrange(int(WIDTH * 0.25), int(WIDTH * 0.75 - enemy_width))
    enemy_start_y = -600
    enemy_speed = 1

    score = 0
    crashed = False

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -car_speed
                if event.key == pygame.K_RIGHT:
                    x_change = car_speed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        screen.fill(GRASS)  # Fill background with green

        # Draw the road
        pygame.draw.rect(screen, BLACK, [WIDTH * 0.25, 0, WIDTH * 0.5, HEIGHT])

        # Draw the yellow dotted line
        line_width = 5
        line_length = 20
        gap_length = 20
        x_position = WIDTH * 0.5
        y_position = 0

        while y_position < HEIGHT:
            pygame.draw.line(screen, YELLOW, (x_position, y_position), (x_position, y_position + line_length), line_width)
            y_position += line_length + gap_length

        draw_enemy(enemy_start_x, enemy_start_y)
        enemy_start_y += enemy_speed

        enemy_speed += .001
        draw_car(x, y)

        # Boundaries for the player's car
        if x < WIDTH * 0.25:
            x = WIDTH * 0.25
        elif x > WIDTH * 0.75 - car_width:
            x = WIDTH * 0.75 - car_width

        if enemy_start_y > HEIGHT:
            enemy_start_y = 0 - enemy_height
            enemy_start_x = random.randrange(int(WIDTH * 0.25), int(WIDTH * 0.75 - enemy_width))
            score += 1
            if score >= WINNING_SCORE:
                you_win()

        if y < enemy_start_y + enemy_height:
            if x > enemy_start_x and x < enemy_start_x + enemy_width or x + car_width > enemy_start_x and x + car_width < enemy_start_x + enemy_width:
                crashed = True

        # Display score
        score_text = button_font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.update()

    game_over()

# Start the game
main_menu()
