import random
#Esta es una lista de palabras que pueden ir en el juego a modo de "palabra secreta"
lista_palabras = ["serpiente", "choripan", "sushi", "afrodescendiente", "gaucho", "desestacionalizacion"]

#Selecciona una de las palabras de la lista y la reserva como "palabra secreta"
palabra_secreta = random.choice(lista_palabras)

correctas = set()
incorrectas = set()
intentos_restantes = 6

def mostrar_estado_dejuego():
    #Muestra la palabra secreta cuando todas las letras hayan sido reveladas:
    palabra_mostrada = " ".join([letter if letter in correctas else "_" for letter in palabra_secreta])

    print(f"Palabra: {palabra_mostrada}")
    print(f"Intentos incorrectos:  {' '.join(incorrectas)}")
    print(f"Intentos restantes: {intentos_restantes}")

#Loop principal de juego
while True:
    mostrar_estado_dejuego()
    adivinar = input("Ingresá tu apuesta: ").lower()

    #Chequear si la palabra es correcta:
    if adivinar in palabra_secreta:
        correctas.add(adivinar)
        #Chequear por condición de victoria
        if set(palabra_secreta).issubset(correctas):
            print("Felicidades, has adivinado la palabra")
            break
    else:
        incorrectas.add(adivinar)
        intentos_restantes -= 1
        #chequar condición de derrota
        if intentos_restantes == 0:
            print("Juego terminado!, te quedaste sin intentos!")
            print(f"La palabra secreta era: {palabra_secreta}")
        break