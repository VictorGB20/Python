# Ejercicio 1: Implementa el codigo que, dado un numero aleatorio del 1 al 100, pregunte al usuario
# por un numero y le ofrezca informacion acerca de si ha acertado o fallado. EL programa terminara cuando el usuario acierte
# el numero o cuando se haya dado un numero de intentos erroneos maximos (5).

import random
from unittest import case

def adivina_numero():
    numeroLimite = 5
    numeroIntento = 0
    numeroUsuario = 0
    numeroAdivinar = random.randint(1, 100)
    print(numeroAdivinar)
    while numeroAdivinar != numeroUsuario:
        numeroIntento += 1
        print(f"Intento {numeroIntento}: ")
        numeroUsuario = int(input("Introduzca un numero: "))

        if numeroIntento >= numeroLimite:
            print("Has superado la cantidad de intentos")
            break
        elif numeroUsuario <= numeroAdivinar:
            print("El numero a adivinar es mas grande")
        elif numeroUsuario >= numeroAdivinar:
            print("El numero a adivinar es mas pequeño")
        elif numeroUsuario == numeroAdivinar:
            print("Enhorabuena, lo has adivinado")
        else: 
            print("Intentelo de nuevo")
            
# Ejercicio 2:Implementa una calculadora que haga + - * /. El programa ofrecera un menú con las operaciones
# disponibles y pedira al usuario que introduzca una opcion. Introducira 2 numeros y la orden.

def calculadora():
    print("Calculadora básica")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    accion = int(input("Introduzca la orden (1-4): "))
    
    if accion >= 1 or accion <=4:
        num1 = int(input("Introduce el primer numero: "))
        num2 = int(input("Introduce el segundo numero: "))
        if accion == 1:
            sumar(num1, num2)
        if accion == 2:
            restar(num1, num2)
        if accion == 3:
            multiplicar(num1, num2)
        if accion == 4:
            dividir(num1, num2)   

def sumar(num1, num2):
    print("El resultado es: " + str(num1 + num2))
def restar(num1, num2):
    print("El resultado es: " + str(num1 - num2))
def multiplicar(num1, num2):
    print("El resultado es: " + str(num1 * num2))
def dividir(num1, num2):
    print("El resultado es: " + str(num1 / num2))


# Ejercicio 3: Implementa un traductor de español a codigo morse. Se debe pedir una palabra o frase en
# español y traducir a código morse segun la siguiente tabla. Las palabras se separarán mediante saltos
# de linea y las letras mediante un espacio en blanco.

def codigoMorse():
    morse = {
        'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.',
        'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
        'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
        's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--',
        'x': '-..-', 'y': '-.--', 'z': '--..'
    }
    palabra = input("Introduce una palabra o frase en español: ").lower()
    codigo = ""
    for letra in palabra:
        if letra!= " ":
            codigo += morse[letra] + " "
        else:
            codigo += " "
            print(codigo)
            codigo = ""
    print(codigo)
    print()

# Ejercicio 4: Implementa un programa que lea y almacene en un array una serie de temperaturas que irá
# introduciendo el usuario y ofrezca un menú con la posibilidad de insertar nuevas temperaturas y calcule
# la temperatura media, la mas alta y la mas bja de los valores almacenados en el array. El programa parará
# solo mediante una opcion del menú



# Ejercicio 5: Implementa el juego de hundir la flota. EL tablero consiste en un array de dos dimensiones 10x10
# y llevará asociado un barco que ocupe 3 casillas en horizontal o vertical, pedirá al usuario una posición y
# y ofrezca retroalimentacion para saber si ha dado en agua, ha dado al barco o si despues de varios intentos lo ha hundido.
# El juego tendra un numero maximo de intentos y terminará cuando se sobrepasen o bien, cuando se hunda un barco.
# Al final del juego, se imprimira el tablero con la situacion final.

def hundir_flota():
    tablero = [[0]*5 for _ in range(4)]
    barco = [0, 0, 0]
    intentos = 0
    maxIntentos = 10
    while intentos < maxIntentos:
        print("Intento", intentos+1)
        posicion = input("Introduce una posicion (fila, columna): ").split(",")
        if len(posicion)== 2 or posicion[0].isdigit() or posicion[1].isdigit():
            fila = int(posicion[0])
            columna = int(posicion[1])
            if tablero[fila][columna] == 0:
                tablero[fila][columna] = 1
                intentos += 1
                print("Agua!")
            elif tablero[fila][columna] == 1:
                print("Has dado en agua!")
            else:
                print("Has dado al barco!")
                barco[0] = 1
                barco[1] = 1
                barco[2] = 1
            if barco[0] == 1 and barco[1] == 1 and barco[2] == 1:
                print("Has hundido el barco!")
                break
            print()
            print("Barco:", barco)
            print()
            print("Intentos:", intentos, "/", maxIntentos)
            print()
            print("Tablero:")
            print("\n".join([" ".join(str(x) for x in row) for row in tablero]))
            print()
    print("Has ganado!")
    print()
    print("Barco:", barco)
    print()
    print("Intentos:", intentos, "/", maxIntentos)
    print()
    print("Tablero:")
    print("\n".join([" ".join(str(x) for x in row) for row in tablero]))