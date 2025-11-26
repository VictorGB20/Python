import sys
import emoji

def calculadora(num1, operador, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        print("Los números deben ser válidos.")
        return

    if operador == "+":
        resultado = num1 + num2
    elif operador == "-":
        resultado = num1 - num2
    elif operador == "*":
        resultado = num1 * num2
    elif operador == "/":
        if num2 == 0:
            print("No se puede dividir entre cero.")
            return
        resultado = num1 / num2
    else:
        print(f"Operador '{operador}' no reconocido. Usa +, -, * o /")
        return

    print(f"Resultado: {num1} {operador} {num2} = {resultado}")

def ayuda():
    print("Uso: python calculadora.py <num1> <operador> <num2>")
    print("Ejemplos:")
    print("  python calculadora.py 5 + 3")
    print("  python calculadora.py 10 * 4")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        ayuda()
    else:
        _, num1, operador, num2 = sys.argv
        calculadora(num1, operador, num2)
