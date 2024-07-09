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

imp = pygame.image.load("sherk.png")
imp = pygame.transform.scale(imp, (250, 250))

cr7 = pygame.image.load("Diseño sin título.png")
cr7 = pygame.transform.scale(cr7, (250, 250))

background_image = pygame.image.load("zzv4EXBoonre7Vmc7uweJWtnPJcHewebu3UVVhKPP9eQgcR0s0H_qr9GquXVU3PFdkXoirSLOSYkWjsfHNMqgA.webp")
background_image = pygame.transform.scale(background_image, (width, height)) 

objetivo_size = 100
objetivo_x = random.randint(square_size, width - objetivo_size - square_size)  # Evita que el objetivo esté en los márgenes iniciales del jugador
objetivo_y = random.randint(square_size, height - objetivo_size - square_size)  # Evita que el objetivo esté en los márgenes iniciales del jugador
objetivo_rect = pygame.Rect(objetivo_x, objetivo_y, objetivo_size, objetivo_size)
puntaje = 0

speed = 29 

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

    screen.blit(background_image,(0,0))
    screen.blit(cr7, (700,750))
    screen.blit(imp,(100,100))


    puntaje_texto = font.render("El majestuoso Sherk y el rescate de Fiona ", True, font_color)
    screen.blit(puntaje_texto, (10, 10))

    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
                       