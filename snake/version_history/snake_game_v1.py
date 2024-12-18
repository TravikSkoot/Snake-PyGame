import random
import pygame

# Initialisierung von Pygame
pygame.init()

# Definiere Farben
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Bildschirmgröße
width = 600
height = 400
screen = pygame.display.set_mode((width, height))

# Fenstername
pygame.display.set_caption('Snake Game')

# Uhr und Geschwindigkeit
clock = pygame.time.Clock()
snake_speed = 15

# Snake-Variablen
snake_size = 10
snake_list = []
length_of_snake = 1

# Schriftarten
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Funktion zum Anzeigen des Scores
def display_score(score):
    value = score_font.render("Score: " + str(score), True, yellow)
    screen.blit(value, [0, 0])

# Funktion zur Snake-Zeichnung
def draw_snake(snake_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, black, [x[0], x[1], snake_size, snake_size])

# Nachricht zentriert anzeigen
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    text_rect = mesg.get_rect(center=(width / 2, height / 2))  # Zentriert den Text
    screen.blit(mesg, text_rect)

# Hauptspiel-Schleife
def game_loop():
    game_over = False
    game_close = False

    # Startposition der Snake
    x = width / 2
    y = height / 2

    # Snake-Bewegung
    x_change = 0
    y_change = 0

    # Letzte Bewegungsrichtung (um den Rückwärtsgang zu verhindern)
    last_x_change = 0
    last_y_change = 0

    # Essen-Position
    food_x = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - snake_size) / 10.0) * 10.0

    global length_of_snake
    length_of_snake = 1
    snake_list = []

    while not game_over:

        while game_close:
            screen.fill(blue)
            message("Verloren! Leertaste: Nochmal - Escape: Beenden", red)
            display_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_SPACE:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and last_x_change != snake_size:
                    x_change = -snake_size
                    y_change = 0
                elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and last_x_change != -snake_size:
                    x_change = snake_size
                    y_change = 0
                elif (event.key == pygame.K_UP or event.key == pygame.K_w) and last_y_change != snake_size:
                    y_change = -snake_size
                    x_change = 0
                elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and last_y_change != -snake_size:
                    y_change = snake_size
                    x_change = 0

        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True
        x += x_change
        y += y_change
        screen.fill(blue)
        pygame.draw.rect(screen, green, [food_x, food_y, snake_size, snake_size])

        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(snake_size, snake_list)
        display_score(length_of_snake - 1)

        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
            food_y = round(random.randrange(0, height - snake_size) / 10.0) * 10.0
            length_of_snake += 1

        # Aktualisiere letzte Bewegungsrichtung
        last_x_change = x_change
        last_y_change = y_change

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Spiel starten
game_loop()