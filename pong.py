import pygame
import random

pygame.init()

# Colores
blanco = (255, 255, 255)
negro = (0, 0, 0)

# Configuración de pantalla
ancho_pantalla = 800
alto_pantalla = 600
pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
pygame.display.set_caption('Juego de Pong')

# Configuración del reloj
reloj = pygame.time.Clock()

# Configuración del jugador y la bola
jugador1 = pygame.Rect(50, alto_pantalla // 2 - 60, 10, 120)
bola = pygame.Rect(ancho_pantalla // 2 - 15, alto_pantalla // 2 - 15, 30, 30)
velocidad_bola = [7, 7]

def juego():
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            jugador1.y -= 7
        if keys[pygame.K_s]:
            jugador1.y += 7

        bola.x += velocidad_bola[0]
        bola.y += velocidad_bola[1]

        if bola.top <= 0 or bola.bottom >= alto_pantalla:
            velocidad_bola[1] = -velocidad_bola[1]
        if bola.colliderect(jugador1) or bola.colliderect((ancho_pantalla - jugador1.width, jugador1.y, jugador1.width, jugador1.height)):
            velocidad_bola[0] = -velocidad_bola[0]

        pantalla.fill(negro)
        pygame.draw.rect(pantalla, blanco, jugador1)
        pygame.draw.ellipse(pantalla, blanco, bola)
        pygame.display.flip()
        reloj.tick(60)

if __name__ == "__main__":
    juego()
