# TODO: Poner comentarios
# TODO: Poner warning de mucho velocidad

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

gradient_ground_color1 = (137, 3, 1)
gradient_ground_color2 = (142, 33, 3)

gradient_sky_color1 = (171, 227, 152)
gradient_sky_color2 = (93, 143, 79)

# Grounds
ground_color = (255, 255, 255)

ground1_size = [150, 20]
ground1_pos = [screen_middle_x - ground1_size[0]//2, 500]
ground1 = pygame.Rect(ground1_pos, ground1_size)

# kill obstacles
kill_bottom_color = (255, 0, 0)

kill_bottom_size = [SCREEN.get_rect().x, 10]
kill_bottom_pos = [0, SCREEN.get_rect().bottom]
kill_bottom = pygame.Rect(kill_bottom_pos, kill_bottom_size)

# Checkpoints
checkpoint_color = (230, 190, 130)

points = [
    (10, 500),
    (80, 500),
    (45, 550)
]

current_checkpoint = 0

# Player variables
spawn_point = [ground1.centerx, ground1.top + 10]

player_pos = [ground1.centerx, ground1.top + 10]
player_size = [20, 20]
player_color = (0, 0, 255)  # Blue

player_jetpack_force = -8

player_jump = -12

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
        self.direction = "right"
        self.player_movement = 5

        # Physics variables
        self.vel_y = 0
        self.vel_x = 0
        self.on_ground = True

    def current_fuel(self):
        return self.player_fuel

    def current_direction(self):
        return self.direction

    def update(self, keys, spawn_point):
        if self.on_ground:
            self.player_movement = 8
        if self.player_using_jetpack or not self.on_ground:
            self.player_movement = 3

        if keys[pygame.K_LEFT] | keys[pygame.K_a]:
            self.rect.x -= self.player_movement
            self.direction = "left"
        if keys[pygame.K_RIGHT] | keys[pygame.K_d]:
            self.rect.x += self.player_movement
            self.direction = "right"

        # Jumping logic
        """
        if keys[pygame.K_UP] | keys[pygame.K_w] and self.on_ground:
            self.vel_y = player_jump
            self.on_ground = False
        """

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

        print(self.vel_y)
        if not self.on_ground:
            self.vel_y += 1

        if self.vel_y >= 15 and not self.player_using_jetpack and self.player_fuel <= 0:
            player.rect.x = spawn_point[0]
            player.rect.y = spawn_point[1]


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


def draw_gradient_rect(surface, rect, color1, color2):
    # Create a 2x1 surface with the two colors
    temp_surf = pygame.Surface((1, 2), flags=pygame.SRCALPHA)
    temp_surf.fill(color1, (0, 0, 1, 1))
    temp_surf.fill(color2, (1, 0, 1, 1))

    # Scale it to the target rectangle
    scaled_surf = pygame.transform.smoothscale(temp_surf, (rect.width, rect.height))
    surface.blit(scaled_surf, rect)


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
    player.update(keys, spawn_point)
    player.ground_collision(ground_sprites)
    player.check_kill_player(kill_obstacles, spawn_point)

    # Detect edge
    clamp_rect = pygame.Rect(
        0, -10000, SCREEN.get_width(), SCREEN.get_height() + 10000)
    player.rect.clamp_ip(clamp_rect)

    # Background color
    SCREEN.fill(gradient_sky_color1)

    # Sky gradient
    draw_gradient_rect(SCREEN, pygame.Rect(SCREEN.get_rect().x, SCREEN.get_rect().y, 800, 800), gradient_sky_color1, gradient_sky_color2)

    # Ground gradient
    draw_gradient_rect(SCREEN, pygame.Rect(SCREEN.get_rect().x, 500, 800, 800), gradient_ground_color1, gradient_ground_color2)

    # Draw text
    facing_text = font.render(str(player.current_direction()), True, text_color)
    facing_text_pos = (20, 10)
    SCREEN.blit(facing_text, facing_text_pos)

    fuel_text = font.render(str(player.current_fuel()), True, text_color)
    fuel_text_pos = (20, 40)
    SCREEN.blit(fuel_text, fuel_text_pos)

    # Draw sprites
    player_sprite.draw(SCREEN)
    ground_sprites.draw(SCREEN)
    kill_obstacles.draw(SCREEN)

    # Draw checkpoint
    pygame.draw.polygon(SCREEN, checkpoint_color, points)

    pygame.display.flip()

pygame.quit()
