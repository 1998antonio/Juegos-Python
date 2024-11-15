import pygame
import random

pygame.init()

# Colores
blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)

# Configuración de pantalla
ancho_pantalla = 800
alto_pantalla = 600
pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
pygame.display.set_caption('Rompebloques')

# Configuración del reloj
reloj = pygame.time.Clock()

# Configuración de la plataforma
plataforma = pygame.Rect(ancho_pantalla // 2 - 50, alto_pantalla - 30, 100, 10)
velocidad_plataforma = 7

# Configuración de la bola
bola = pygame.Rect(ancho_pantalla // 2 - 10, alto_pantalla // 2 - 10, 20, 20)
velocidad_bola = [random.choice([-5, 5]), -5]  # Reducimos la velocidad de la bola

# Configuración de los bloques
def crear_bloques(nivel):
    bloques = []
    bloque_ancho = 75
    bloque_alto = 30
    for i in range(8):
        for j in range(5 + nivel):  # Aumenta el número de filas con cada nivel
            bloque = pygame.Rect(i * (bloque_ancho + 10) + 35, j * (bloque_alto + 10) + 35, bloque_ancho, bloque_alto)
            bloques.append(bloque)
    return bloques

bloques = crear_bloques(0)

def mostrar_texto(texto, fuente, color, x, y):
    texto_surface = fuente.render(texto, True, color)
    pantalla.blit(texto_surface, (x, y))

def juego():
    global bloques
    puntuacion = 0
    nivel = 0
    pausa = False
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_r:
                    plataforma.x = ancho_pantalla // 2 - 50
                    bola.x = ancho_pantalla // 2 - 10
                    bola.y = alto_pantalla // 2 - 10
                    velocidad_bola[0] = random.choice([-5, 5])
                    velocidad_bola[1] = -5
                    bloques = crear_bloques(nivel)
                    puntuacion = 0
                if evento.key == pygame.K_p:
                    pausa = not pausa

        if not pausa:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and plataforma.left > 0:
                plataforma.x -= velocidad_plataforma
            if keys[pygame.K_RIGHT] and plataforma.right < ancho_pantalla:
                plataforma.x += velocidad_plataforma

            bola.x += velocidad_bola[0]
            bola.y += velocidad_bola[1]

            if bola.top <= 0 or bola.colliderect(plataforma):
                velocidad_bola[1] = -velocidad_bola[1]
            if bola.left <= 0 or bola.right >= ancho_pantalla:
                velocidad_bola[0] = -velocidad_bola[0]

            for bloque in bloques[:]:
                if bola.colliderect(bloque):
                    bloques.remove(bloque)
                    puntuacion += 1
                    velocidad_bola[1] = -velocidad_bola[1]
                    break

            pantalla.fill(negro)
            pygame.draw.rect(pantalla, verde, plataforma)
            pygame.draw.ellipse(pantalla, rojo, bola)
            for bloque in bloques:
                pygame.draw.rect(pantalla, azul, bloque)
            
            mostrar_texto(f"Puntuación: {puntuacion}", pygame.font.SysFont("bahnschrift", 25), blanco, 10, 10)
            mostrar_texto("Presiona 'R' para reiniciar", pygame.font.SysFont("bahnschrift", 25), blanco, 10, 40)
            mostrar_texto("Presiona 'P' para pausar", pygame.font.SysFont("bahnschrift", 25), blanco, 10, 70)

            if len(bloques) == 0:
                nivel += 1
                bloques = crear_bloques(nivel)
                bola.x = ancho_pantalla // 2 - 10
                bola.y = alto_pantalla // 2 - 10
                velocidad_bola[0] = random.choice([-5, 5])
                velocidad_bola[1] = -5
                mostrar_texto(f"Nivel {nivel} completado! Presiona 'R' para reiniciar", pygame.font.SysFont("bahnschrift", 50), blanco, ancho_pantalla // 6, alto_pantalla // 2)

            pygame.display.flip()
            reloj.tick(60)

if __name__ == "__main__":
    juego()
