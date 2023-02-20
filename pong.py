import pygame

# Initialize Pygame
pygame.init()

# Set the dimensions of the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Set the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create the game window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Pong Game')

# Set up the paddles
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 60
PADDLE_SPEED = 5

player_paddle = pygame.Rect(50, WINDOW_HEIGHT / 2 - PADDLE_HEIGHT / 2, PADDLE_WIDTH, PADDLE_HEIGHT)
opponent_paddle = pygame.Rect(WINDOW_WIDTH - 50 - PADDLE_WIDTH, WINDOW_HEIGHT / 2 - PADDLE_HEIGHT / 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Set up the ball
BALL_SIZE = 10
BALL_SPEED = 5

ball = pygame.Rect(WINDOW_WIDTH / 2 - BALL_SIZE / 2, WINDOW_HEIGHT / 2 - BALL_SIZE / 2, BALL_SIZE, BALL_SIZE)
ball_speed_x = BALL_SPEED
ball_speed_y = BALL_SPEED

# Set up the game clock
clock = pygame.time.Clock()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    # Move the paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player_paddle.y > 0:
        player_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_s] and player_paddle.y < WINDOW_HEIGHT - PADDLE_HEIGHT:
        player_paddle.y += PADDLE_SPEED
    if keys[pygame.K_UP] and opponent_paddle.y > 0:
        opponent_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and opponent_paddle.y < WINDOW_HEIGHT - PADDLE_HEIGHT:
        opponent_paddle.y += PADDLE_SPEED
    
    # Move the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    # Check for collisions with the paddles
    if ball.colliderect(player_paddle) or ball.colliderect(opponent_paddle):
        ball_speed_x *= -1
    
    # Check for collisions with the top and bottom of the window
    if ball.y < 0 or ball.y > WINDOW_HEIGHT - BALL_SIZE:
        ball_speed_y *= -1
    
    # Check for a score
    if ball.x < 0 or ball.x > WINDOW_WIDTH - BALL_SIZE:
        ball.x = WINDOW_WIDTH / 2 - BALL_SIZE / 2
        ball.y = WINDOW_HEIGHT / 2 - BALL_SIZE / 2
        ball_speed_x *= -1
    
    # Clear the screen
    window.fill(BLACK)
    
    # Draw the paddles and ball
    pygame.draw.rect(window, WHITE, player_paddle)
    pygame.draw.rect(window, WHITE, opponent_paddle)
    pygame.draw.ellipse(window, WHITE, ball)
    
    # Update the screen
    pygame.display.update()
    
    # Set the game clock
    clock.tick(60)
