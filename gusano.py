import pygame
import time
import random

# Inicializamos pygame
pygame.init()

# Definimos colores
blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (255, 0, 0)
verde = (0, 255, 0)

# Dimensiones de la pantalla
ancho_pantalla = 600
alto_pantalla = 400 
pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
pygame.display.set_caption('Juego del Gusano')

# Tamaño del bloque del gusano
bloque_gusano = 10
reloj = pygame.time.Clock()

# Velocidad del gusano
velocidad_gusano = 15

# Fuente del texto
fuente = pygame.font.SysFont("bahnschrift", 25)

def mostrar_puntuacion(puntuacion):
    valor = fuente.render("Puntuación: " + str(puntuacion), True, blanco)
    pantalla.blit(valor, [0, 0])

def nuestro_gusano(bloque_gusano, lista_gusano):
    for x in lista_gusano:
        pygame.draw.rect(pantalla, verde, [x[0], x[1], bloque_gusano, bloque_gusano])

def mensaje_final(msg, color):
    mensaje = fuente.render(msg, True, color)
    pantalla.blit(mensaje, [ancho_pantalla / 6, alto_pantalla / 3])

def bucle_juego():
    game_over = False
    game_close = False

    # Posición inicial del gusano
    x_gusano = ancho_pantalla / 2
    y_gusano = alto_pantalla / 2

    # Cambio en la posición (velocidad)
    cambio_x = 0
    cambio_y = 0

    # Lista para representar el cuerpo del gusano
    lista_gusano = []
    largo_gusano = 1

    # Posición de la comida
    x_comida = round(random.randrange(0, ancho_pantalla - bloque_gusano) / 10.0) * 10.0
    y_comida = round(random.randrange(0, alto_pantalla - bloque_gusano) / 10.0) * 10.0

    while not game_over:

        while game_close:
            pantalla.fill(negro)
            mensaje_final("Perdiste! Presiona Q-Quit o C-Continuar", rojo)
            mostrar_puntuacion(largo_gusano - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        bucle_juego()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    cambio_x = -bloque_gusano
                    cambio_y = 0
                elif event.key == pygame.K_RIGHT:
                    cambio_x = bloque_gusano
                    cambio_y = 0
                elif event.key == pygame.K_UP:
                    cambio_y = -bloque_gusano
                    cambio_x = 0
                elif event.key == pygame.K_DOWN:
                    cambio_y = bloque_gusano
                    cambio_x = 0

        # Verificamos si el gusano choca con los bordes
        if x_gusano >= ancho_pantalla or x_gusano < 0 or y_gusano >= alto_pantalla or y_gusano < 0:
            game_close = True

        # Movemos el gusano
        x_gusano += cambio_x
        y_gusano += cambio_y
        pantalla.fill(negro)

        # Dibujamos la comida
        pygame.draw.rect(pantalla, rojo, [x_comida, y_comida, bloque_gusano, bloque_gusano])

        # Actualizamos el cuerpo del gusano
        cabeza_gusano = []
        cabeza_gusano.append(x_gusano)
        cabeza_gusano.append(y_gusano)
        lista_gusano.append(cabeza_gusano)
        if len(lista_gusano) > largo_gusano:
            del lista_gusano[0]

        # Verificamos si el gusano choca consigo mismo
        for x in lista_gusano[:-1]:
            if x == cabeza_gusano:
                game_close = True

        nuestro_gusano(bloque_gusano, lista_gusano)
        mostrar_puntuacion(largo_gusano - 1)

        pygame.display.update()

        # Si el gusano "come" la comida
        if x_gusano == x_comida and y_gusano == y_comida:
            x_comida = round(random.randrange(0, ancho_pantalla - bloque_gusano) / 10.0) * 10.0
            y_comida = round(random.randrange(0, alto_pantalla - bloque_gusano) / 10.0) * 10.0
            largo_gusano += 1

        # Velocidad del juego
        reloj.tick(velocidad_gusano)

    pygame.quit()
    quit()

bucle_juego()