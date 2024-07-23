import pygame
import sys
import random

pygame.init()

width, height = 1800, 920
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Historia de shrek")

background_color = (0, 0, 0)
font_color = (255, 255, 255)

square_size = 250
x = width // 20 - square_size // 20
y = height // 20 - square_size // 20
player_rect = pygame.Rect(x, y, square_size, square_size)

imp = pygame.image.load("sherk.png")
imp = pygame.transform.scale(imp, (250, 250))

cr7 = pygame.image.load("Diseño sin título.png")
cr7 = pygame.transform.scale(cr7, (250, 250))

shrek = pygame.image.load ("png-clipart-shrek-shrek-thumbnail-removebg-preview.png")
shrek = pygame.transform.scale(shrek, (250, 250))

estado = "inicio"

primer= pygame.image.load("pixelcut-export.jpeg")
primer = pygame.transform.scale(primer, (width, height)) 

background_image = pygame.image.load("pixelcut-export.jpeg")
background_image = pygame.transform.scale(background_image, (width, height)) 

texto1 = pygame.image.load ("Organizador Grafico Conceptual Doodle Multicolor.png")
texto1 = pygame.transform.scale(texto1, (width, height))

bienvenida= pygame.image.load ("onion.png")
bienvenida= pygame.transform.scale(bienvenida, (width, height))

pantano = pygame.image.load("Captura de pantalla 2024-07-15 105556.png")
pantano = pygame.transform.scale(pantano, (width, height)) 

siquiero = pygame.image.load("garro.png")
siquiero = pygame.transform.scale(siquiero, (width, height)) 

noquiero = pygame.image.load("noquiero.png")
noquiero = pygame.transform.scale(noquiero, (width, height))

finalno=pygame.image.load("finalno.png")
finalno = pygame.transform.scale(finalno, (width, height))

nv=pygame.image.load("nv1.png")
nv = pygame.transform.scale(nv, (width, height))

noburro=pygame.image.load("burritosi.png")
noburro = pygame.transform.scale(noburro, (width, height))

burris= pygame.image.load("noburropreg.png")
burris = pygame.transform.scale(burris, (width, height))

npburro=pygame.image.load("fondosi.png")
npburro = pygame.transform.scale(npburro, (width, height))

noveno=pygame.image.load("9.png")
noveno = pygame.transform.scale(noveno, (width, height))

decimo=pygame.image.load("10.png")
decimo = pygame.transform.scale(decimo, (width, height))

once=pygame.image.load("11.png")
once = pygame.transform.scale(once, (width, height))

doce=pygame.image.load("12.png")
doce = pygame.transform.scale(doce, (width, height))

trece=pygame.image.load("13.png")
trece = pygame.transform.scale(trece, (width, height))

catorce=pygame.image.load("14.png")
catorce = pygame.transform.scale(catorce, (width, height))

quince=pygame.image.load("15.png")
quince = pygame.transform.scale(quince, (width, height))

dieseis=pygame.image.load("16.png")
dieseis = pygame.transform.scale(dieseis, (width, height))

diesiete=pygame.image.load("17.png")
diesiete = pygame.transform.scale(diesiete, (width, height))

diesocho=pygame.image.load("18.png")
diesocho = pygame.transform.scale(diesocho, (width, height))

diesnueve=pygame.image.load("19.png")
diesnueve = pygame.transform.scale(diesnueve, (width, height))

veinte=pygame.image.load("20.png")
veinte = pygame.transform.scale(veinte, (width, height))

veinteuno=pygame.image.load("21.png")
veinteuno = pygame.transform.scale(veinteuno, (width, height))

veintecuatro=pygame.image.load("24.png")
veintecuatro = pygame.transform.scale(veintecuatro, (width, height))

veintecinco=pygame.image.load("25.png")
veintecinco = pygame.transform.scale(veintecinco, (width, height))

veintesies=pygame.image.load("26.png")
veinteseis = pygame.transform.scale(veintesies, (width, height))

veintesiete=pygame.image.load("27.png")
veintesiete = pygame.transform.scale(veintesiete, (width, height))

veinteocho=pygame.image.load("28.png")
veinteocho = pygame.transform.scale(veinteocho, (width, height))

veintenueve=pygame.image.load("29.png")
veintenueve = pygame.transform.scale(veintenueve, (width, height))

treinta=pygame.image.load("30.png")
treinta = pygame.transform.scale(treinta, (width, height))

treintados=pygame.image.load("32.png")
treintados = pygame.transform.scale(treintados, (width, height))

treintatres=pygame.image.load("33.png")
treintatres = pygame.transform.scale(treintatres, (width, height))

treintacuatro=pygame.image.load("34.png")
treintacuatro = pygame.transform.scale(treintacuatro, (width, height))

treintacinco=pygame.image.load("35.png")
treintacinco = pygame.transform.scale(treintacinco, (width, height))

treintaseis=pygame.image.load("36.png")
treintaseis = pygame.transform.scale(treintaseis, (width, height))

treintasiete=pygame.image.load("37.png")
treintasiete = pygame.transform.scale(treintasiete, (width, height))

treintaocho=pygame.image.load("38.png")
treintaocho = pygame.transform.scale(treintaocho, (width, height))

treintanueve=pygame.image.load("39.png")
treintanueve = pygame.transform.scale(treintanueve, (width, height))

cuarenta=pygame.image.load("40.png")
cuarenta = pygame.transform.scale(cuarenta, (width, height))

cuarentados=pygame.image.load("42.png")
cuarentados = pygame.transform.scale(cuarentados, (width, height))

cuarentatres=pygame.image.load("43.png")
cuarentatres = pygame.transform.scale(cuarentatres, (width, height))

cuarentacuatro=pygame.image.load("44.png")
cuarentacuatro = pygame.transform.scale(cuarentacuatro, (width, height))

cuarentacinco=pygame.image.load("45.png")
cuarentacinco = pygame.transform.scale(cuarentacinco, (width, height))

cuarentaseis=pygame.image.load("46.png")
cuarentasies = pygame.transform.scale(cuarentaseis, (width, height))

cuarentasiete=pygame.image.load("47.png")
cuarentasiete = pygame.transform.scale(cuarentasiete, (width, height))

cuarentaocho=pygame.image.load("48.png")
cuarentaocho = pygame.transform.scale(cuarentaocho, (width, height))

cuarentanueve=pygame.image.load("49.png")
cuarentanueve = pygame.transform.scale(cuarentanueve, (width, height))

objetivo_size = 100
objetivo_x = random.randint(square_size, width - objetivo_size - square_size)  # Evita que el objetivo esté en los márgenes iniciales del jugador
objetivo_y = random.randint(square_size, height - objetivo_size - square_size)  # Evita que el objetivo esté en los márgenes iniciales del jugador
objetivo_rect = pygame.Rect(objetivo_x, objetivo_y, objetivo_size, objetivo_size)
puntaje = 0


font = pygame.font.Font(None, 80)

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

                elif estado =="veintecuatro":
                    estado = "veintecinco"
                elif estado == "veintecinco":
                    estado = "veinteseis"
                elif estado == "veinteseis":
                    estado = "veintesiete"
                elif estado == "veintesiete":
                    estado = "veinteocho"
                elif estado == "veinteocho":
                    estado = "veintenueve"
                elif estado == "veintenueve":
                    estado = "treinta"


                elif estado =="treintacinco":
                    estado = "treintaseis"
                elif estado == "treintaseis":
                    estado = "treintasiete"
                elif estado == "treintasiete":
                    estado = "treintaocho"
                elif estado == "treintaocho":
                    estado = "treintanueve"
                elif estado == "treintanueve":
                    estado = "cuarenta"

                elif estado =="treintados":
                    estado = "treintatres"
                elif estado =="treintatres":
                    estado  ="treintacuatro"

                elif estado == "cuarentados":
                    estado = "cuarentatres"
                elif estado == "cuarentatres":
                    estado = "cuarentacuatro"
                elif estado == "cuarrentacuatro":
                    estado = "cuarentacinco"

                elif estado =="cuarentaseis":
                    estado = "cuarentasiete"
                elif estado == "cuarentasiete":
                    estado = "cuarentaocho"
                elif estado == "cuarrentaocho":
                    estado = "cuarentanueve"

                elif estado =="nv":
                    estado = "burris"

                elif estado == "npburro":
                    estado = "noveno"
                elif estado == "noveno":
                    estado = "decimo"
                elif estado == "decimo":
                    estado = "once"

                elif estado =="noburro":
                    estado = "doce"
                elif estado =="doce":
                    estado = "trece"


                elif estado =="catorce":
                    estado = "quince"
                elif estado =="quince":
                    estado = "dieseis"

                elif estado =="diesiete":
                    estado = "diesocho"
                elif estado =="diesocho":
                    estado = "diesnueve"
                elif estado =="diesnueve":
                    estado = "veinte"
                elif estado =="veinte":
                    estado = "veinteuno"

            if event.key == pygame.K_1:   
                if estado=="pantano": 
                    estado="siquiero1" 
                elif estado=="siquiero1":
                    estado="treintados"
                elif estado == "noquiero":
                    estado = "finalsi"
                elif estado == "noquiero1":
                    estado = "finalno"
                elif estado == "burris":
                    estado = "noburro"
                elif estado == "trece":
                    estado = "diesiete"
                elif estado == "treintacuatro":
                    estado = "treintacinco"

            if event.key == pygame.K_2:
                if estado=="siquiero1":
                    estado="veintecuatro"
                elif estado=="pantano":
                    estado="noquiero1" 
                elif estado== "noquiero1":
                    estado="nv"
                elif estado == "burris":
                    estado = "npburro"  
                elif estado == "trece":
                    estado = "catorce"  
                elif estado == "treintacuatro":
                    estado = "cuarentados"        


               
                


    if estado == "inicio":
        screen.blit(primer,(0,0))
        puntaje_texto = font.render("El majestuoso Sherk y el inesperado rescate ", True, (10,10,10,))
        screen.blit(puntaje_texto, (500, 0))
        
    if estado == "texto1":
        screen.blit(texto1,(0,0))

    
    if estado == "bienvenida":
        screen.blit(bienvenida,(0,0))

    if estado == "pantano":
        screen.blit(pantano,(0,0))
        screen.blit(shrek, (400,550))
        loas= font.render("Fiona esta en problemas, un dragon la secuestro en su castillo ", True, (255,255,255,))
        screen.blit(loas, (5, 0))
        loasi= font.render("y necesita tu ayuda ", True, (255,255,255,))
        screen.blit(loasi, (5, 60))
        asi= font.render("Quieres ir a rescatarla? ", True, (255,255,255,))
        screen.blit(asi, (500, 120))
        si= font.render("1. Si, aca comenzamos una nueva etapa, ahora camina al bosque. ", True, (255,255,255,))
        screen.blit(si, (5, 200))
        nop=font.render(".2 no? ", True, (255,255,255,))
        screen.blit(nop, (5, 260))

    if estado == "siquiero1":
        screen.blit(siquiero,(0,0))

    if estado == "noquiero1":
        screen.blit(noquiero,(0,0))

    if estado == "finalno":
        screen.blit(finalno,(0,0))

    if estado == "noburro":
        screen.blit(noburro,(0,0))

    if estado == "npburro":
        screen.blit(npburro,(0,0))
       
    if estado == "burris":
        screen.blit(burris,(0,0))

    if estado == "nv":
        screen.blit(nv,(0,0))

    if estado == "noveno":
        screen.blit(noveno,(0,0))

    if estado == "decimo":
        screen.blit(decimo,(0,0))

    if estado == "once":
        screen.blit(once,(0,0))

    if estado == "doce":
        screen.blit(doce,(0,0))
       
    if estado == "trece":
        screen.blit(trece,(0,0))

    if estado == "catorce":
        screen.blit(catorce,(0,0))

    if estado == "quince":
        screen.blit(quince,(0,0))

    if estado == "dieseis":
        screen.blit(dieseis,(0,0))

    if estado == "diesiete":
        screen.blit(diesiete,(0,0))

    if estado == "diesocho":
        screen.blit(diesocho,(0,0))
       
    if estado == "diesnueve":
        screen.blit(diesnueve,(0,0))

    if estado == "veinte":
        screen.blit(veinte,(0,0))

    if estado == "veinteuno":
        screen.blit(veinteuno,(0,0))

    if estado == "veintecuatro":
        screen.blit(veintecuatro,(0,0))
       
    if estado == "veintecinco":
        screen.blit(veintecinco,(0,0))

    if estado == "veinteseis":
        screen.blit(veinteseis,(0,0))

    if estado == "veintesiete":
        screen.blit(veintesiete,(0,0))

    if estado == "veinteocho":
        screen.blit(veinteocho,(0,0))

    if estado == "veintenueve":
        screen.blit(veintenueve,(0,0))

    if estado == "treinta":
        screen.blit(treinta,(0,0))
       
    if estado == "treintados":
        screen.blit(treintados,(0,0))

    if estado == "treintatres":
        screen.blit(treintatres,(0,0))
    
    if estado == "treintacuatro":
        screen.blit(treintacuatro,(0,0))
       
    if estado == "treintacinco":
        screen.blit(treintacinco,(0,0))

    if estado == "treintaseis":
        screen.blit(treintaseis,(0,0))

    if estado == "treintasiete":
        screen.blit(treintasiete,(0,0))
       
    if estado == "treintaocho":
        screen.blit(treintaocho,(0,0))

    if estado == "treintanueve":
        screen.blit(treintanueve,(0,0))

    if estado == "cuarenta":
        screen.blit(cuarenta,(0,0))

    if estado == "cuarentados":
        screen.blit(cuarentados,(0,0))

    if estado == "cuarentatres":
        screen.blit(cuarentatres,(0,0))

    if estado == "cuarentacuatro":
        screen.blit(cuarentacuatro,(0,0))
    
    if estado == "cuarentacinco":
        screen.blit(cuarentacinco,(0,0))

    if estado == "cuarentaseis":
        screen.blit(cuarentaseis,(0,0))

    if estado == "cuarentasiete":
        screen.blit(cuarentasiete,(0,0))

    if estado == "cuarentaocho":
        screen.blit(cuarentaocho,(0,0))

    if estado == "cuarentanueve":
        screen.blit(cuarentanueve,(0,0))


    pygame.display.flip()

    pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()
                       