import pygame
import random
import os

pygame.mixer.init()

pygame.init()

# Colours
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
screen_width = 900
screen_height = 600

# Creating Window

gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Background image
bgimg = pygame.image.load("D:\GIT and Programming\my python projects\CV projects\Snake Game\Background Images\Background.jpg")
bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()
HS = pygame.image.load("D:\GIT and Programming\my python projects\CV projects\Snake Game\Background Images\HomeScreen.jpg")
HS = pygame.transform.scale(HS, (screen_width, screen_height)).convert_alpha()
GO = pygame.image.load("D:\GIT and Programming\my python projects\CV projects\Snake Game\Background Images\GameOver.jpg")
GO = pygame.transform.scale(GO, (screen_width, screen_height)).convert_alpha()

# Game Title
pygame.display.set_caption("Snake Game")
pygame.display.update()

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)


def screen_score(text, color, x, y):
    text_screen = font.render(text, True, color)
    gameWindow.blit(text_screen, [x, y])


def plot_snake(gameWindow, color, snake_list, snake_size):
    for x, y in snake_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill(white)
        gameWindow.blit(HS, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # pygame.mixer.music.load("back.mp3")
                    # pygame.mixer.music.play()
                    GameLoop()
        pygame.display.update()
        clock.tick(60)


# Game Loop
def GameLoop():
    # Game specific variable
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    snake_size = 10
    fps = 40
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(0, screen_width)
    food_y = random.randint(0, screen_height)
    score = 0
    init_velocity = 5
    snake_list = []
    snake_length = 1
    # check if high score file exists
    if not os.path.exists("highscore"):
        with open("highscore", "w") as f:
            f.write("0")
    with open("highscore", "r") as f:
        highscore = f.read()

    while not exit_game:
        if game_over:
            with open("highscore", "w") as f:
                f.write(str(highscore))
            gameWindow.blit(GO, (0, 0))
            screen_score("Score " + str(score), red, 400, 450)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
                    # cheat code
                    if event.key == pygame.K_q:
                        score = score + 10
            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
            if abs(snake_x - food_x) < 6 and abs(snake_y - food_y) < 6:
                score = score + 10
                print(f"score: {score}")

                food_x = random.randint(10, screen_width - 10)
                food_y = random.randint(50, screen_height - 10)
                snake_length = snake_length + 5
                if score > int(highscore):
                    highscore = score

            gameWindow.fill(white)
            gameWindow.blit(bgimg, (0, 0))
            screen_score("Score: " + str(score) + "High Score: " + str(highscore), red, 5, 5)
            # pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list) > snake_length:
                del snake_list[0]
            if head in snake_list[:-1]:
                game_over = True
                # pygame.mixer.music.load("gameover.mp3")
                # pygame.mixer.music.play()

            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True
                # pygame.mixer.music.load("gameover.mp3")
                # pygame.mixer.music.play()
            plot_snake(gameWindow, black, snake_list, snake_size)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()


welcome()
# GameLoop()
