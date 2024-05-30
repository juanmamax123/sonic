import pygame
import sys
import random

pygame.init()

width, height = 1800, 920
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Juego del cuadrado móvil")

background_color = (0, 0, 0)
font_color = (255, 255, 255)

square_size = 60
x = width // 2 - square_size // 2
y = height // 2 - square_size // 2
player_rect = pygame.Rect(x, y, square_size, square_size)

imp = pygame.image.load("Lionel_Messi_WC2022.jpg")
imp = pygame.transform.scale(imp, (90, 90))

cr7 = pygame.image.load("cristiano-ronaldo-triste.jpg")
cr7 = pygame.transform.scale(cr7, (90, 90))

background_image = pygame.image.load("pngtree-aerial-aerial-aerial-view-of-football-field-picture-image_1683356.png")
background_image = pygame.transform.scale(background_image, (width, height)) 

objetivo_size = 100
objetivo_x = random.randint(square_size, width - objetivo_size - square_size)  # Evita que el objetivo esté en los márgenes iniciales del jugador
objetivo_y = random.randint(square_size, height - objetivo_size - square_size)  # Evita que el objetivo esté en los márgenes iniciales del jugador
objetivo_rect = pygame.Rect(objetivo_x, objetivo_y, objetivo_size, objetivo_size)
puntaje = 0

speed = 5 

proyectil_speed = 15
proyectil_width = 5
proyectil_height = 5
proyectiles = []


font = pygame.font.Font(None, 36)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                proyectil = pygame.Rect(x + square_size // 2, y + square_size // 2, proyectil_width, proyectil_height)
                proyectiles.append(proyectil)


    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed

    if y < 0:
        y = 0


    for proyectil in proyectiles:
        proyectil.x += proyectil_speed
        if proyectil.x > width:
            proyectiles.remove(proyectil)


    for proyectil in proyectiles:
        if cr7.get_rect(topleft=(objetivo_x, objetivo_y)).colliderect(proyectil):
            proyectiles.remove(proyectil)
            puntaje += 1
            objetivo_x = random.randint(0, width - objetivo_size)
            objetivo_y = random.randint(0, height - objetivo_size)
            objetivo_rect.topleft = (objetivo_x, objetivo_y)


    screen.blit(background_image,(0,0))
    for proyectil in proyectiles:
        pygame.draw.rect(screen, (255, 255, 255), proyectil)
    pygame.draw.rect(screen, (255, 0, 0), (x, y, square_size, square_size))
    screen.blit(imp, (x, y))
    screen.blit(cr7, (objetivo_x, objetivo_y))
    
    if puntaje == 10:
        running = False  # Esto detiene el juego cuando el puntaje llega a 10
        break

    puntaje_texto = font.render("Puntaje: " + str(puntaje), True, font_color)
    screen.blit(puntaje_texto, (10, 10))

    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
