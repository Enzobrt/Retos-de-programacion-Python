import pygame
import keyboard

pygame.init()

screen_width = 1000
screen_height = 1000

screen = pygame.display.set_mode([screen_width, screen_height])

# Sirve para cambiarle el nombre a la ventana
pygame.display.set_caption('Mars Mars')

white = (255, 255, 255)

player_color = (255, 30, 70)

characterX = 10
player_Y = 10
player_width = 50
player_height = 50
player = pygame.Rect(characterX, player_Y, player_width, player_height)
pygame.draw.rect(screen, player_color, player)


character_image = pygame.image.load("elmo.jpg")
character_rect = character_image.get_rect()
character_rect.center = (100, 100)

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

    if keyboard.is_pressed('left'):
        character_rect.x -= 5
    if keyboard.is_pressed('right'):
        character_rect.x += 5
    if keyboard.is_pressed('up'):
        character_rect.y -= 5
    if keyboard.is_pressed('down'):
        character_rect.y += 5

    # Update the screen
    screen.fill((255, 255, 255))
    screen.blit(character_image, character_rect)
    pygame.display.flip()

pygame.Quit()
