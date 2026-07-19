import pygame
import sys
import random
# Initialize Pygame
pygame.init()

# Font of the game
score_font = pygame.font.SysFont("Consolas", 24, bold=True)
game_over_text_font = pygame.font.SysFont("Impact", 40)
restart_font = pygame.font.SysFont("Trebuchetms", 20)
running = True

# Window size
WIDTH, HEIGHT = 800, 600    

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set window title
pygame.display.set_caption("Snake Game")

# Create a clock
clock = pygame.time.Clock()

#Snake
START_SNAKE = [
        [100,100], 
        [80,100], 
        [60,100],
        [40,100]
]
snake = [segment.copy() for segment in START_SNAKE]
#Food
food_x = random.randrange(0, WIDTH, 20)
food_y = random.randrange(0, HEIGHT, 20)

#Game update
game_over = False

# Speed of the snake
snake_speed = 20  
#Movement of snake
direction = "Right"
#Points you scored
score = 0

def restart_game():
    # Reset everything :
        global snake        
        global score
        global food_x
        global food_y
        global direction
        global game_over
        snake = [segment.copy() for segment in START_SNAKE]
        score = 0
        direction = "Right"
        food_x = random.randrange(0, WIDTH, 20)
        food_y = random.randrange(0, HEIGHT, 20)
        game_over = False


def event_handle():
    global direction
    # Check for events
    global running
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
                    running = False
        elif event.type == pygame.KEYDOWN:
                   
            if event.key == pygame.K_RIGHT:
                    if direction != "Left":
                            direction = "Right"

            elif event.key == pygame.K_LEFT:
                    if direction != "Right":
                            direction = "Left"

            elif event.key == pygame.K_UP:
                    if direction != "Down":
                            direction = "Up"

            elif event.key == pygame.K_DOWN:
                    if direction != "Up":
                            direction = "Down"
            if event.key == pygame.K_r and game_over:
                   restart_game()
            elif event.key == pygame.K_ESCAPE and game_over:
                running = False
      
def draw_game():
        global score
        global game_over
    # Draw snake
        for segment in snake:
            pygame.draw.rect(screen, (0, 255, 0),(segment[0], segment[1], 20, 20))
    # Draw Food
        pygame.draw.rect(screen, (255, 0, 0), (food_x, food_y, 20, 20) )
    # Say Score
        score_text = score_font.render(f"Score: {score}", True,(220,220,220))
        screen.blit(score_text, (WIDTH - 180, 10))
        # Wall collison                                                                          and self-collison
        if (snake[0][0] < 0 or snake[0][0] >= WIDTH or snake[0][1] < 0 or snake[0][1] >= HEIGHT) or (snake[0] in snake[1:]):
                game_over = True
    
        if game_over:
                game_over_text = game_over_text_font.render(f"Oops! Game Over. You've scored : {score}", True, (255,51,51))
                screen.blit(game_over_text, (120,200))

                restart1 = restart_font.render(f"Do You Want to Restart the Game?", True, (255,153,153))
                restart2 = restart_font.render(f"If yes, Press r. If no, press escape", True, (255,153,153))
                screen.blit(restart1,(230, 300))
                screen.blit(restart2,(235, 320))

def update_game():
    
        global game_over
        global score
        global food_x
        global food_y
    #The body wwill follow the head
        for i in range(len(snake)-1, 0, -1):
            snake[i] = snake[i-1].copy()
    #If direction is Right the snake moves to right
        if direction == "Right":
            snake[0][0] += snake_speed
    
    #If direction is Left the snake moves to Left
        elif direction == "Left":
            snake[0][0] -= snake_speed

    #If direction is Right the snake moves to Upward
        elif direction == "Up":
            snake[0][1] -= snake_speed
    
    #If direction is Down the snake moves toward Down
        elif direction == "Down":
            snake[0][1] += snake_speed
        screen.fill((30, 30, 36))
    # Check if snake and food at the same place
        if snake[0][0] == food_x and snake[0][1] == food_y:
        # Increase the score
                score += 10
        # Snake will get bigger after eating
                snake.append(snake[-1].copy())
        # New food will spawn in a random plce in a window
                food_x = random.randrange(0, WIDTH, 20)
                food_y = random.randrange(0, HEIGHT, 20)
# Main game loop
while running:

    event_handle()

    if not game_over:
            update_game()
    
    
    draw_game()


    # Update the display
    pygame.display.flip()
    
    # Limit to 60 FPS
    clock.tick(10)

# Quit Pygame
pygame.quit()
# Display Score on the terminal
print(f"You scored : {score}")
# Exits the game
sys.exit()