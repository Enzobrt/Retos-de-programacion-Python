import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
running = True

playerColor = (255, 0, 0)
playerRect = [50, 50 , 10, 10]

while running:
    pygame.draw.rect(screen, playerColor, playerRect)
    pygame.draw.rect(screen, (255, 255, 255), (100, 100, 100, 100))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    screen.fill((0, 0, 0))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
