import pygame
import sys

# inicializar pygame
pygame.init()

# configuracion de la ventana
width, height = 640, 480
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("juego del cuadrado movil")

#color del fondo
background_color = (0,0,0)
#tamaño y posocion inicial del ciadradp
square_size= 50
x = width // 2 - square_size//2
y = height //2 - square_size//2
#velocidad de movimiento del cuadradp
speed = 5

#bucle princial del juego
running= True
while running:
    for event in pygame.event.grt():
        if event.type==pygame.quit:
            running = False

#detectar teclas presionadas
keys = pygame.key.get_pressed()
if keys[pygame.k_up]:
    y -= speed #mueve el cuadrado hacia arriba

# mantener el cuadrado dentro de los limites superiores de la pantalla
if y<0:
    y=0

    #rellenar el fondo y dibujar el cuadrado
    screen.fill(background_color)
    pygame.draw.rec(screen,(255,0,0),(x,y,square_size,square_size))

    #actualizar la pantalla
    pygame.display.flip

    # controlar la velocidad del bucle
    pygame.time.clock().tick(60)

#salir de pygame
pygame.quit()
sys.exit()