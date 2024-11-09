import random
from datetime import datetime  # Für Zeitstempel in Debug-Nachrichten
import pygame

# Debug-Modus aktivieren oder deaktivieren
debug_mode = True

# Initialisierung von Pygame
pygame.init()

# Definiere Farben
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
orange = (255, 165, 0)  # Neue Farbe
purple = (160, 32, 240)  # Neue Farbe
pink = (255, 105, 180)  # Neue Farbe
light_blue = (173, 216, 230)  # Neue Farbe

# Setze Hintergrundfarbe
background_color = blue

# Bildschirmgröße
width = 600
height = 400
screen = pygame.display.set_mode((width, height))

# Fenstername
pygame.display.set_caption('Snake Game')

# Uhr und Geschwindigkeit
clock = pygame.time.Clock()

# Snake-Variablen
snake_color = green
snake_size = 10
snake_list = []
length_of_snake = 1
default_snake_speed = 15  # Ursprüngliche Geschwindigkeit

# Food & Powerup Variablen
food_color = red
powerup_color_1 = blue
powerup_color_2 = orange
powerup_color_3 = purple


# Neue Schriftarten für den Game-Over-Bildschirm
large_font_style = pygame.font.SysFont("comic sans ms", 50)  # Große Schrift
small_font_style = pygame.font.SysFont("comic sans ms", 25)  # Kleinere Schrift

# Angepasste Funktion für den Game-Over-Bildschirm
def game_over_message(high_score):
    screen.fill(background_color)

    # Große Nachricht "GAME OVER!"
    game_over_text = large_font_style.render("GAME OVER!", True, red)
    verlor_rect = game_over_text.get_rect(center=(width / 2, height / 4))
    screen.blit(game_over_text, verlor_rect)

    # Kleinere Nachricht "Highscore"
    highscore_text = small_font_style.render(f"Highscore: {high_score}", True, yellow)
    highscore_rect = highscore_text.get_rect(center=(width / 2, height / 2 - 30))
    screen.blit(highscore_text, highscore_rect)

    # Kleinere Nachricht "Nochmal: Leertaste"
    nochmal_text = small_font_style.render("Nochmal: Leertaste", True, yellow)
    nochmal_rect = nochmal_text.get_rect(center=(width / 2, height / 2))
    screen.blit(nochmal_text, nochmal_rect)

    # Kleinere Nachricht "Beenden: Escape"
    beenden_text = small_font_style.render("Beenden: Escape", True, yellow)
    beenden_rect = beenden_text.get_rect(center=(width / 2, (height / 2) + 50))
    screen.blit(beenden_text, beenden_rect)

    pygame.display.update()

# 🟢 Funktion zum Anzeigen des Power-up-Timers
def display_powerup_timer(boost_timer, duration):
    remaining_time = max(0, (duration - (pygame.time.get_ticks() - boost_timer)) // 1000)
    timer_text = small_font_style.render(f"Power-up Zeit: {remaining_time}s", True, yellow)
    screen.blit(timer_text, [width - 250, 0])  # Anzeige oben rechts

# Highscore speichern und laden
def load_high_score():
    try:
        with open("../highscore.txt", "r") as file:
            return int(file.read())
    except (FileNotFoundError, ValueError):
        return 0  # Wenn die Datei nicht existiert oder leer ist


def save_high_score(score):
    with open("../highscore.txt", "w") as file:
        file.write(str(score))


# Schriftarten
font_style = pygame.font.SysFont("comic sans ms", 25)
score_font = pygame.font.SysFont("calibri", 35)


# Funktion zum Anzeigen des Scores und des Highscores
def display_score(score, high_score):
    value = score_font.render("Score: " + str(score) + "  Highscore: " + str(high_score), True, yellow)
    screen.blit(value, [0, 0])


# Funktion zur Snake-Zeichnung
def draw_snake(snake_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, snake_color, [x[0], x[1], snake_size, snake_size])


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
def handle_powerups(x, y, powerup_active, powerup_x, powerup_y, powerup_type, boost_timer, invincible):
    # Power-up Typen: 1 = Speed Boost, 2 = Slowness, 3 = Unsterblichkeit
    if powerup_type == 1:  # Speed Boost
        pygame.draw.rect(screen, powerup_color_1, [powerup_x, powerup_y, snake_size, snake_size])  # Power-up als rotes Quadrat
        if x == powerup_x and y == powerup_y:
            powerup_active = True
            boost_timer = pygame.time.get_ticks()
            log_debug_message(f"Power-up collected: Speed Boost at {powerup_x}, {powerup_y}")
            powerup_x, powerup_y = None, None  # Entferne Power-up

    elif powerup_type == 2:  # Slowness
        pygame.draw.rect(screen, powerup_color_2, [powerup_x, powerup_y, snake_size, snake_size])
        if x == powerup_x and y == powerup_y:
            powerup_active = True
            boost_timer = pygame.time.get_ticks()
            log_debug_message(f"Power-up collected: Slowness at {powerup_x}, {powerup_y}")
            powerup_x, powerup_y = None, None

    elif powerup_type == 3:  # Unsterblichkeit
        pygame.draw.rect(screen, powerup_color_3, [powerup_x, powerup_y, snake_size, snake_size])  # Power-up als gelbes Quadrat
        if x == powerup_x and y == powerup_y:
            invincible = True
            boost_timer = pygame.time.get_ticks()
            log_debug_message(f"Power-up collected: Invincibility at {powerup_x}, {powerup_y}")
            powerup_x, powerup_y = None, None  # Entferne Power-up

    return powerup_active, powerup_x, powerup_y, powerup_type, boost_timer, invincible


def apply_powerup_effects(powerup_active, snake_speed, boost_timer, default_speed, powerup_type, invincible):
    # Wenn der Speed Boost aktiv ist
    if powerup_active and powerup_type == 1:
        snake_speed = 25
        if pygame.time.get_ticks() - boost_timer > 5000:  # 5 Sekunden Boost
            powerup_active = False
            snake_speed = default_speed

    # Wenn das Slowness-Item aktiv ist
    elif powerup_active and powerup_type == 2:
        snake_speed = 5
        if pygame.time.get_ticks() - boost_timer > 5000:
            powerup_active = False
            snake_speed = default_speed

    # Unsterblichkeitseffekt
    elif invincible:
        if pygame.time.get_ticks() - boost_timer > 5000:  # 5 Sekunden Unsterblichkeit
            invincible = False

    return powerup_active, snake_speed, invincible


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

    global length_of_snake

    # Highscore laden beim Start
    high_score = load_high_score()

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
    invincible = False  # Unsterblichkeitsstatus

    # Power-up Timer & Item Pool
    item_pool = [1, 2, 3]  # 1 = Speed Boost, 2 = Slowness, 3 = Unsterblichkeit
    last_spawn_time = 0
    next_spawn_interval = random.randint(10000, 30000)  # 10 bis 30 Sekunden
    spawn_timer = 0  # Timer für das Verschwinden des Power-ups

    while not game_over:

        while game_close:
            # 🟢 Überprüfen, ob der aktuelle Score größer ist als der Highscore
            if length_of_snake - 1 > high_score:
                high_score = length_of_snake - 1
                save_high_score(high_score)  # 🟢 Speichern des neuen Highscores

            game_over_message(high_score)  # Zeige den Game-Over-Bildschirm mit der neuen Funktion

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
                        invincible = False
                        spawn_timer = 0
                        last_spawn_time = pygame.time.get_ticks()  # Setze den letzten Spawn-Timer auf den aktuellen Zeitpunkt
                        length_of_snake = 1  # Zurücksetzen der Snake-Länge
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

        # 🟢 Durch-die-Wand-Effekt für Unsterblichkeitsstatus:
        if invincible:
            if x >= width:
                x = 0
            elif x < 0:
                x = width - snake_size
            if y >= height:
                y = 0
            elif y < 0:
                y = height - snake_size
        else:
            if x >= width or x < 0 or y >= height or y < 0:
                game_close = True

        x += x_change
        y += y_change

        # 🟢 Hintergrund zeichnen
        screen.fill(background_color)

        pygame.draw.rect(screen, food_color, [food_x, food_y, snake_size, snake_size])

        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                if not invincible:  # Wenn Unsterblichkeit aktiv ist, keine Kollisionen beachten
                    game_close = True

        draw_snake(snake_size, snake_list)

        # Update Fenstertitel mit aktuellem Score, Highscore und FPS (wenn im Debug-Modus)
        if debug_mode:
            fps = clock.get_fps()
            pygame.display.set_caption(
                f"Snake Game - Score: {length_of_snake - 1}  Highscore: {high_score}  FPS: {fps:.2f}")
        else:
            pygame.display.set_caption(f"Snake Game - Score: {length_of_snake - 1}  Highscore: {high_score}")

        display_score(length_of_snake - 1, high_score)

        # Power-up Handling
        if powerup_x is not None and powerup_y is not None:
            powerup_active, powerup_x, powerup_y, powerup_type, boost_timer, invincible = handle_powerups(
                x, y, powerup_active, powerup_x, powerup_y, powerup_type, boost_timer, invincible
            )

            # Überprüfen, ob das Power-up schon länger als der Timer existiert
            time_elapsed = pygame.time.get_ticks() - last_spawn_time
            if time_elapsed >= spawn_timer:
                powerup_x, powerup_y = None, None  # Entferne das Power-up nach Ablauf des Timers

        # Power-up Spawning (wenn kein Power-up aktiv ist)
        if not powerup_active and powerup_x is None and powerup_y is None:
            powerup_x, powerup_y, powerup_type, last_spawn_time, next_spawn_interval, spawn_timer = spawn_powerup(
                item_pool, last_spawn_time, next_spawn_interval, powerup_active, spawn_timer
            )

        # Power-up Effekte anwenden und Timer anzeigen
        powerup_active, snake_speed, invincible = apply_powerup_effects(
            powerup_active, snake_speed, boost_timer, default_snake_speed, powerup_type, invincible
        )

        if powerup_active or invincible:
            display_powerup_timer(boost_timer, 5000)  # 🟢 5000 ms = 5 Sekunden Power-up Dauer

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