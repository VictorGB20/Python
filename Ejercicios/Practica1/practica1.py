# practica1.py

#  Ejercicio 1: Entrada de usuario y tipos de datos

# nombre = input("Ingresa tu nombre: ")
# edad = int(input("Ingresa tu edad: "))
# altura = float(input("Ingresa tu altura en metros (ej: 1.70): "))

# Ejercicio 4: Manejo de errores

nombre = input("Ingresa tu nombre: ")

while True: #verifica si es un numero entero
    try:
        edad = int(input("Ingresa tu edad: "))
        break
    except ValueError:
        print("Por favor, introduce un número entero para la edad.")

while True: #verifica si es un numero decimal
    try:
        altura = float(input("Ingresa tu altura en metros (ej: 1.70): "))
        break
    except ValueError:
        print("Por favor, introduce un número decimal válido para la altura.")

#imprime datos
print(f"Hola {nombre}, tienes {edad} años y mides {altura} metros.")
print("Tipo de nombre:", type(nombre))
print("Tipo de edad:", type(edad))
print("Tipo de altura:", type(altura))


#  Ejercicio 2: Funciones básicas

def saludar(nombre):    #recoge nombre y lo imprime
    return f"Hola {nombre}, ¡bienvenido!"

def calcularImc(peso, altura): #recoge peso/altura y calcula imc
    return peso / (altura ** 2)

#llama funciones e imprime
print(saludar(nombre))
peso = float(input("Ingresa tu peso en kg: "))
imc = calcularImc(peso, altura)
print(f"Tu IMC es {imc:.2f}")


#  Ejercicio 3: Función con valores por defecto y *args

def presentarPersona(nombre="Usuario", edad=None, *aficiones): #creamos funcion que recoja datos e imprima
    mensaje = f"{nombre} tiene {edad} años"
    if aficiones:
        mensaje += " y le gusta: " + ", ".join(aficiones)
    print(mensaje)

#Ejemplos
presentarPersona("Ana", 25, "leer", "correr", "viajar")
presentarPersona("Luis", 30)
presentarPersona()


#  Ejercicio 5: Función con emoji

#importamos libreria
import emoji

def calcularImcConEmoji(peso, altura):  #creamos funcion para imprimir imc con if
    imc = peso / (altura ** 2)
    if imc < 18.5:
        estado = "Bajo peso " + emoji.emojize(":warning:", language="alias")
    elif imc < 25:
        estado = "Normal " + emoji.emojize(":smile:", language="alias")
    else:
        estado = "Sobrepeso " + emoji.emojize(":exclamation:", language="alias")
    return imc, estado

#llamamos alas funciones
imc, estado = calcularImcConEmoji(peso, altura)
print(f"Tu IMC es {imc:.2f} -> {estado}")


#  Ejercicio 7: Lista de números

#creamos variables
entrada = input("Ingresa números separados por coma: ")
numeros = [int(x) for x in entrada.split(",")]

suma = sum(numeros)
promedio = suma / len(numeros)
maximo = max(numeros)
minimo = min(numeros)

#imprimimos datos
print(f"La suma es {suma}, el promedio es {promedio}, el máximo {maximo}, el mínimo {minimo}")


