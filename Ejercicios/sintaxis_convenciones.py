
"""
En esta seccion, importaremos archivos externos

"""

import operaciones


"""
Este es el primer programa, vamos a practicar la sintaxis basica de Python
y las convenciones de escritura.
"""
print("Hola Mundo")  # Imprime un mensaje en la consola
# Definicion de variables
mi_variable = 10  # Variable entera
mi_variable_flotante = 20.5  # Variable flotante
mi_variable_cadena = "Hola"  # Variable cadena
mi_variable_booleana = True  # Variable booleana
# Uso de una funcion
print(type(mi_variable))  # Imprime el tipo de la variable
print(type(mi_variable_flotante))  # Imprime el tipo de la variable
print(type(mi_variable_cadena))  # Imprime el tipo de la variable
print(type(mi_variable_booleana))  # Imprime el tipo de la variable

print("Edad",type (mi_variable), mi_variable)  # Imprime la edad y su tipo

lista1 = [1, 2, 3, 4, 5]  # Definicion de una lista
print("Lista", type(lista1), lista1)  # Imprime la lista y su tipo
print(lista1[2])  # Imprime el tercer elemento de la lista

#tuplas
tupla1 = (1, 2, 3, 4, 5)  # Definicion de una tupla
print("Tupla", type(tupla1), tupla1)  # Imprime la tupla y su tipo

#diccionarios
midiccionario = {
    "nombre":"Paquito",
    "apellido":"Chocolatero",
    "usuario":"chocopaquito",
    "contraseña":"1234"
    }  # Definicion de un diccionario
print(midiccionario["nombre"])  # Imprime el diccionario y su tipo

#conjuntos
conjunto1 = {1, 2, 3, 4, 5}  # Definicion de un conjunto
conjunto2 = {4, 5, 5, 7, 8}  # Conjunto repetido
print("Conjunto",conjunto1)  # Imprime el conjunto
print("Conjunto2",conjunto2)  # Imprime el conjunto

#Conversion de tipos
int("10")       # 10 (toma una cadena y devuelve un número entero)
str(20)         # "20" (toma un número entero y devuelve una cadena)
float("3.14")   # 3.14 (toma una cadena y devuelve un número decimal)

#introducir datos por teclado
numero1 = int(input("Introduce un numero: "))  # Toma un dato por teclado
numero2 = int(input("Introduce otro numero: "))  # Toma un dato por teclado y lo convierte a entero
# print("Numero:", numero1)  # Imprime el numero
# print("Numero2:", numero2)  # Imprime el numero2
# print("Suma:", numero1 + numero2)  # Imprime la suma de los numeros como cadena


#If
if numero1 > numero2:
    print("El numero1(", numero1 ,") es mayor que el numero2 (", numero2 ,")")
elif numero1 < numero2:
    print("El numero1(", numero1 ,") es menor que el numero2 (", numero2 ,")")
else:
    print("Los numeros son iguales")

#Match
match numero1:
    case 1:
        print("El numero es 1")
    case 2:
        print("El numero es 2")
    case 3 | 4 | 5:
        print("El numero es 3, 4 o 5")
    case _:
        print("El numero no es 1, 2, 3, 4 o 5")

#Bucles for
for i in range(5):  # Bucle for
    print("Bucle for:", i)  # Imprime el valor de i

words = ["Hola", "Mundo", "Python", "Es", "Genial"]  # Lista de palabras
for word in words:  # Bucle for
    print("Palabra:", word)  # Imprime la palabra

#Bucles while
contador = 0  # Inicializa el contador
while contador < 5:  # Bucle while
    print("Bucle while:", contador)  # Imprime el valor del contador
    contador += 1  # Incrementa el contador
print("Fin del bucle while")  # Imprime un mensaje






