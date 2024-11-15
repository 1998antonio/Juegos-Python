import random

def juego_adivinanza():
    numero_secreto = random.randint(1, 100)
    intentos = 0

    print("¡Bienvenido al juego de adivinanza!")
    print("He seleccionado un número entre 1 y 100. ¿Puedes adivinar cuál es?")

    while True:
        intento = int(input("Ingresa tu adivinanza: "))
        intentos += 1

        if intento < numero_secreto:
            print("Demasiado bajo.")
        elif intento > numero_secreto:
            print("Demasiado alto.")
        else:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            break

if __name__ == "__main__":
    juego_adivinanza()
