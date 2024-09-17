import pygame
import time
import random
from datetime import datetime  # Für Zeitstempel in Debug-Nachrichten

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
default_snake_speed = 15  # Ursprüngliche Geschwindigkeit

# Snake-Variablen
snake_size = 10
snake_list = []
length_of_snake = 1

# Highscore-Variable 🟢
high_score = 0

# Schriftarten
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


# Funktion zum Anzeigen des Scores und des Highscores 🟢
def display_score(score, high_score):
    value = score_font.render("Score: " + str(score) + "  Highscore: " + str(high_score), True, yellow)
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


# Log-Funktion für Debug-Nachrichten mit Zeitstempel
def log_debug_message(message):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{timestamp}] {message}")


# Power-up Section
def handle_powerups(x, y, powerup_active, powerup_x, powerup_y, powerup_type, boost_timer):
    # Power-up Typen: 1 = Speed Boost, 2 = Slow Down, etc.
    if powerup_type == 1:  # Speed Boost
        pygame.draw.rect(screen, red, [powerup_x, powerup_y, snake_size, snake_size])  # Power-up als rotes Quadrat
        if x == powerup_x and y == powerup_y:
            powerup_active = True
            boost_timer = pygame.time.get_ticks()
            log_debug_message(f"Power-up collected: Speed Boost at {powerup_x}, {powerup_y}")  # Debug message

            # Setze die Power-up-Koordinaten auf None, damit es verschwindet
            powerup_x, powerup_y = None, None

    return powerup_active, powerup_x, powerup_y, powerup_type, boost_timer


def apply_powerup_effects(powerup_active, snake_speed, boost_timer, default_speed):
    # Wenn der Speed Boost aktiv ist
    if powerup_active:
        snake_speed = 25  # Erhöhte Geschwindigkeit
        if pygame.time.get_ticks() - boost_timer > 5000:  # 5 Sekunden Boost
            powerup_active = False
            snake_speed = default_speed  # Normale Geschwindigkeit
    return powerup_active, snake_speed


# Item Pool Logik
def spawn_powerup(item_pool, last_spawn_time, next_spawn_interval, powerup_active, spawn_timer):
    current_time = pygame.time.get_ticks()

    # Prüfe, ob genug Zeit vergangen ist und kein Power-up aktiv ist, um ein neues zu spawnen
    if not powerup_active and current_time - last_spawn_time >= next_spawn_interval:
        # Wähle ein zufälliges Power-up aus dem Pool
        powerup_type = random.choice(item_pool)

        # Wähle zufällige Positionen für das Power-up
        powerup_x = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
        powerup_y = round(random.randrange(0, height - snake_size) / 10.0) * 10.0

        # Debug message: Welches Power-up spawnt und wo
        log_debug_message(f"Power-up spawned: Type {powerup_type} at {powerup_x}, {powerup_y}")

        # Setze den Timer für den nächsten Spawn (zwischen 10 und 30 Sekunden)
        next_spawn_interval = random.randint(10000, 30000)  # in Millisekunden (10-30 Sekunden)
        spawn_timer = random.randint(3000, 9000)  # 1 bis 3 Sekunden für das Power-up

        # Aktualisiere die Zeit des letzten Spawns
        last_spawn_time = current_time

        return powerup_x, powerup_y, powerup_type, last_spawn_time, next_spawn_interval, spawn_timer

    # Falls kein Power-up gespawnt wird, gib den aktuellen Timer zurück
    return None, None, None, last_spawn_time, next_spawn_interval, spawn_timer


# Hauptspiel-Schleife
def game_loop():
    game_over = False
    game_close = False

    global high_score  # 🟢 Highscore als globale Variable verwenden
    global length_of_snake

    # Initialisierung der Snake-Geschwindigkeit beim Start oder Respawn
    global snake_speed
    snake_speed = default_snake_speed  # Stelle sicher, dass die Geschwindigkeit zurückgesetzt wird

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

    snake_list = []

    # Power-up Variablen
    powerup_active = False
    powerup_x, powerup_y = None, None
    powerup_type = None
    boost_timer = 0

    # Power-up Timer & Item Pool
    item_pool = [1]  # Füge hier weitere Power-ups hinzu (z. B. 2 für Slow Down)
    last_spawn_time = 0
    next_spawn_interval = random.randint(10000, 30000)  # 10 bis 30 Sekunden
    spawn_timer = 0  # Timer für das Verschwinden des Power-ups

    while not game_over:

        while game_close:
            screen.fill(blue)
            # 🟡 Aktualisiere den Highscore, falls der aktuelle Score größer ist
            if length_of_snake - 1 > high_score:
                high_score = length_of_snake - 1

            message("Verloren! Leertaste: Nochmal - Escape: Beenden", red)
            # 🟡 Zeige Highscore zusammen mit dem aktuellen Score
            display_score(length_of_snake - 1, high_score)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_SPACE:
                        # Rücksetzen der Power-up-Variablen beim Neustart
                        powerup_active = False
                        powerup_x, powerup_y = None, None
                        powerup_type = None
                        boost_timer = 0
                        spawn_timer = 0
                        last_spawn_time = pygame.time.get_ticks()  # Setze den letzten Spawn-Timer auf den aktuellen Zeitpunkt
                        # 🟢 Zurücksetzen der Snake-Länge beim Neustart
                        length_of_snake = 1
                        game_loop()  # Neustart des Spiels

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Escape-Taste für Beenden jederzeit
                    game_over = True
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
        display_score(length_of_snake - 1, high_score)

        # Power-up Handling
        if powerup_x is not None and powerup_y is not None:
            powerup_active, powerup_x, powerup_y, powerup_type, boost_timer = handle_powerups(
                x, y, powerup_active, powerup_x, powerup_y, powerup_type, boost_timer
            )

            # Überprüfen, ob das Power-up schon länger als der Timer existiert
            time_elapsed = pygame.time.get_ticks() - last_spawn_time
            if time_elapsed >= spawn_timer:
                log_debug_message(f"Power-up disappeared after {time_elapsed / 1000:.2f} seconds")  # Dauer in Sekunden
                powerup_x, powerup_y = None, None  # Entferne das Power-up nach Ablauf des Timers

        # Power-up Spawning (wenn kein Power-up aktiv ist)
        if not powerup_active and powerup_x is None and powerup_y is None:
            powerup_x, powerup_y, powerup_type, last_spawn_time, next_spawn_interval, spawn_timer = spawn_powerup(
                item_pool, last_spawn_time, next_spawn_interval, powerup_active, spawn_timer
            )

        # Power-up Effekte anwenden
        powerup_active, snake_speed = apply_powerup_effects(
            powerup_active, snake_speed, boost_timer, default_snake_speed
        )

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
