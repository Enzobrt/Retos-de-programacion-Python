import pygame
import numpy as np
# import keyboard

pygame.init()

SCREEN_SIZE = (800, 600)
SCREEN = pygame.display.set_mode(SCREEN_SIZE)
# Sirve para cambiarle el nombre a la ventana
pygame.display.set_caption('Mars Mars')

screen_middle_x = SCREEN.get_rect().centerx
screen_middle_y = SCREEN.get_rect().centery

# Font
font = pygame.font.SysFont("JetBrains Mono", 15)
text_color = (255, 255, 255)  # White

# Background
background = (40, 40, 40)  # Dark gray

# Grounds
ground_color = (255, 255, 255)

ground1_pos = [screen_middle_x/2, 500]
ground1_size = [400, 20]
ground1 = pygame.Rect(ground1_pos, ground1_size)

# kill obstacles
kill_bottom_color = (255, 0, 0)

kill_bottom_size = [SCREEN.get_rect().x, 10]
kill_bottom_pos = [0, SCREEN.get_rect().bottom]
kill_bottom = pygame.Rect(kill_bottom_pos, kill_bottom_size)

# Player variables
player_pos = [screen_middle_x, screen_middle_y]
player_size = [20, 20]
player_color = (0, 0, 255)  # Blue

player_jetpack_force = -8

player_jump = -12
facing = "up"
spawn_point = [screen_middle_x, screen_middle_y]

gravity = 0.5


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Create a simple blue rectangle as the player
        self.image = pygame.Surface(player_size)
        self.image.fill(player_color)
        self.rect = self.image.get_rect()
        self.rect.center = player_pos
        self.alive = True
        self.player_fuel = 100
        self.player_using_jetpack = False

        # Physics variables
        self.vel_y = 0
        self.on_ground = True

    def current_fuel(self):
        return self.player_fuel

    def update(self, keys):
        # Horizontal movement (optional)
        if keys[pygame.K_LEFT] | keys[pygame.K_a]:
            self.rect.x -= 5
            facing = "left"
        if keys[pygame.K_RIGHT] | keys[pygame.K_d]:
            self.rect.x += 5
            facing = "right"

        # Jumping logic
        if keys[pygame.K_UP] | keys[pygame.K_w] and self.on_ground:
            self.vel_y = player_jump
            self.on_ground = False

        # Jetpack logic
        if keys[pygame.K_SPACE] and self.player_fuel > 0:
            self.vel_y = player_jetpack_force
            self.player_fuel -= 1
            self.player_using_jetpack = True
        else:
            self.player_using_jetpack = False

        if self.on_ground and not self.player_using_jetpack:
            self.player_fuel = 100

        # Apply gravity
        self.vel_y += gravity
        self.rect.y += self.vel_y

    def ground_collision(self, grounds):
        self.on_ground = False
        hit = pygame.sprite.spritecollideany(player, grounds)
        if hit and player.vel_y >= 0:
            player.rect.bottom = hit.rect.top
            player.vel_y = 0
            player.on_ground = True

    def check_kill_player(self, kill_obstacles, spawn_point):
        for kill_obstacle in kill_obstacles:
            if self.rect.bottom >= kill_obstacle.rect.top:
                player.rect.x = spawn_point[0]
                player.rect.y = spawn_point[1]


class Ground(pygame.sprite.Sprite):
    def __init__(self, rect):
        super().__init__()
        self.image = pygame.Surface(rect.size)
        self.image.fill(ground_color)
        self.rect = rect


class KillObstacle(pygame.sprite.Sprite):
    def __init__(self, rect):
        super().__init__()
        self.image = pygame.Surface(rect.size)
        self.image.fill(kill_bottom_color)
        self.rect = rect


player = Player()

ground1 = Ground(ground1)
ground_sprites = pygame.sprite.Group([ground1])

kill_bottom = KillObstacle(kill_bottom)
kill_obstacles = pygame.sprite.Group([kill_bottom])

player_sprite = pygame.sprite.Group(player)

# Set up the clock
clock = pygame.time.Clock()
FPS = 60

# Set the game loop
running = True
while running:
    dt = clock.tick(FPS) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    keys = pygame.key.get_pressed()

    # Player functions
    player.update(keys)
    player.ground_collision(ground_sprites)
    player.check_kill_player(kill_obstacles, spawn_point)

    # Detect edge
    clamp_rect = pygame.Rect(
        0, -10000, SCREEN.get_width(), SCREEN.get_height() + 10000)
    player.rect.clamp_ip(clamp_rect)

    # Background color
    SCREEN.fill(background)

    # Draw text
    facing_text = font.render(facing, True, text_color)
    facing_text_pos = (20, 10)
    SCREEN.blit(facing_text, facing_text_pos)

    fuel_text = font.render(str(player.current_fuel()), True, text_color)
    fuel_text_pos = (20, 40)
    SCREEN.blit(fuel_text, fuel_text_pos)

    # Draw sprites
    player_sprite.draw(SCREEN)
    ground_sprites.draw(SCREEN)
    kill_obstacles.draw(SCREEN)

    pygame.display.flip()

pygame.quit()
