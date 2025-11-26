# Ejercicio 1: Implementa el codigo que, dado un numero aleatorio del 1 al 100, pregunte al usuario
# por un numero y le ofrezca informacion acerca de si ha acertado o fallado. EL programa terminara cuando el usuario acierte
# el numero o cuando se haya dado un numero de intentos erroneos maximos (5).
# 
# Ejercicio 2: Implementa una calculadora que haga + - * /. El programa ofrecera un menú con las operaciones
# disponibles y pedira al usuario que introduzca una opcion. Introducira 2 numeros y la orden.
# 
# 
# Ejercicio 3: Implementa un traductor de español a codigo morse. Se debe pedir una palabra o frase en
# español y traducir a código morse segun la siguiente tabla. Las palabras se separarán mediante saltos
# de linea y las letras mediante un espacio en blanco.
# 
# 
# Ejercicio 4: Implementa un programa que lea y almacene en un array una serie de temperaturas que irá
# introduciendo el usuario y ofrezca un menú con la posibilidad de insertar nuevas temperaturas y calcule
# la temperatura media, la mas alta y la mas bja de los valores almacenados en el array. El programa parará
# solo mediante una opcion del menú
#
#
# Ejercicio 5: Implementa el juego de hundir la flota. EL tablero consiste en un array de dos dimensiones 10x10
# y llevará asociado un barco que ocupe 3 casillas en horizontal o vertical, pedirá al usuario una posición y
# y ofrezca retroalimentacion para saber si ha dado en agua, ha dado al barco o si despues de varios intentos lo ha hundido.
# El juego tendra un numero maximo de intentos y terminará cuando se sobrepasen o bien, cuando se hunda un barco.
# Al final del juego, se imprimira el tablero con la situacion final.
#
#

import modulo as m

def main():
    '''
        Mostrar numero aleatorio
    '''
    m.hundir_flota()
    

#llamar función principal
if __name__ == "__main__":
    main()
