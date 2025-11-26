#  Ejercicio 8: Argumentos desde la linea de comandos

#importamos librerias
import sys

#creamos funcion
def main():
    print("Argumentos recibidos:", sys.argv)

    if len(sys.argv) > 1:   #si se reciben datos
        nombre = sys.argv[1]
        if len(sys.argv) >= 4:
            while True: #verifica si es un numero entero
                try:
                    edad = int(sys.argv[2])
                    break
                except ValueError:
                    print("Por favor, introduce un número entero para la edad en el segundo parametro.")
                    return
            ciudad = sys.argv[3]
            print(f"Hola {nombre}, tienes {edad} años y vives en {ciudad}")
        else:   
            print(f"Hola, {nombre}")
    else:   #si no recibe datos
        print("No se proporcionó ningún argumento. Introduzca los parametros con el formato: Nombre Edad Ciudad")

#llamamos funcion
if __name__ == "__main__":
    main()
