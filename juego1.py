import pygame
import sys

pygame.init()

width, height= 640,480
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("juego del cuadrado movil")

background_color = (0,0,0)

square_size = 50
x= width // 2 - square_size // 2
y = height // 2 - square_size // 2

speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            running= False
    
    keys = pygame.key.get_pressed()
    if keys [pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed  
    if keys[pygame.K_LEFT]:
        x -= speed  
    if keys[pygame.K_RIGHT]:
        x += speed  

    if y < 0:
        y = 0

    screen.fill(background_color)
    pygame.draw.rect(screen,(255,0,0),(x,y, square_size,square_size))

    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()