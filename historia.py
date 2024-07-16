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

shrek = pygame.image.load ("png-clipart-shrek-shrek-thumbnail-removebg-preview.png")
shrek = pygame.transform.scale(shrek, (250, 250))

estado = "inicio"

primer= pygame.image.load("previews_0012_custom_1682997344.3685.jpg")
primer = pygame.transform.scale(primer, (width, height)) 


background_image = pygame.image.load("zzv4EXBoonre7Vmc7uweJWtnPJcHewebu3UVVhKPP9eQgcR0s0H_qr9GquXVU3PFdkXoirSLOSYkWjsfHNMqgA.webp")
background_image = pygame.transform.scale(background_image, (width, height)) 


texto1 = pygame.image.load ("Organizador Grafico Conceptual Doodle Multicolor.png")
texto1 = pygame.transform.scale(texto1, (width, height))

bienvenida= pygame.image.load ("shrekamor.png")
bienvenida= pygame.transform.scale(bienvenida, (width, height))

pantano = pygame.image.load("Captura de pantalla 2024-07-15 105556.png")
pantano = pygame.transform.scale(pantano, (width, height)) 


objetivo_size = 100
objetivo_x = random.randint(square_size, width - objetivo_size - square_size)  # Evita que el objetivo esté en los márgenes iniciales del jugador
objetivo_y = random.randint(square_size, height - objetivo_size - square_size)  # Evita que el objetivo esté en los márgenes iniciales del jugador
objetivo_rect = pygame.Rect(objetivo_x, objetivo_y, objetivo_size, objetivo_size)
puntaje = 0


font = pygame.font.Font(None, 36)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print (estado)
                if estado=="inicio":
                    estado="bienvenida"
                elif estado== "bienvenida":
                    estado ="texto1"
                elif estado== "texto1":
                   estado ="pantano"
                     


    if estado == "inicio":
        screen.blit(primer,(0,0))
        puntaje_texto = font.render("El majestuoso Sherk y el rescate de Fiona ", True, (130,203,136,))
        screen.blit(puntaje_texto, (550, 700))
        
    if estado == "texto1":
        screen.blit(texto1,(0,0))

    
    if estado == "bienvenida":
        screen.blit(bienvenida,(0,0))

    if estado == "pantano":
        screen.blit(pantano,(0,0))
        screen.blit(shrek, (400,550))
    
        
    

    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
                       